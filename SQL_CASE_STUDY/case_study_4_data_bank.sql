-- Case Study 4: Data Bank

-- Question 1: How many unique nodes are there on the Data Bank system?

SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;


-- Question 2: What is the number of nodes per region?

SELECT
    r.region_name,
    COUNT(DISTINCT c.node_id) AS node_count
FROM customer_nodes c
JOIN regions r
    ON c.region_id = r.region_id
GROUP BY r.region_name;


-- Question 3: How many customers are allocated to each region?

SELECT
    r.region_name,
    COUNT(DISTINCT c.customer_id) AS customer_count
FROM customer_nodes c
JOIN regions r
    ON c.region_id = r.region_id
GROUP BY r.region_name;


-- Question 4: How many days on average are customers reallocated to a different node?

SELECT
    ROUND(AVG(DATEDIFF(end_date, start_date)), 2) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date <> '9999-12-31';


-- Question 5: What is the median, 80th and 95th percentile for reallocation days in each region?

WITH node_days AS (
    SELECT
        region_id,
        DATEDIFF(end_date, start_date) AS reallocation_days
    FROM customer_nodes
    WHERE end_date <> '9999-12-31'
)
SELECT *
FROM node_days;


-- Customer Transactions

-- Question 6: What is the unique count and total amount for each transaction type?

SELECT
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type;


-- Question 7: What is the average total historical deposit counts and amounts for all customers?

WITH deposits AS (
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)
SELECT
    ROUND(AVG(deposit_count), 2) AS avg_deposit_count,
    ROUND(AVG(deposit_amount), 2) AS avg_deposit_amount
FROM deposits;


-- Question 8: For each month, how many customers make more than 1 deposit and either 1 purchase or 1 withdrawal?

WITH monthly_transactions AS (
    SELECT
        customer_id,
        EXTRACT(MONTH FROM txn_date) AS month_no,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id,
             EXTRACT(MONTH FROM txn_date)
)
SELECT
    month_no,
    COUNT(*) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month_no
ORDER BY month_no;
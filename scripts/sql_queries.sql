-- Sales by Category
SELECT Category, SUM(Sales)
FROM sales
GROUP BY Category;

-- Sales by Year
SELECT strftime('%Y', Order_Date) AS Year, SUM(Sales)
FROM sales
GROUP BY Year;

--Profit by Category

SELECT Category, SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category;

--Top 10 Products by Sales

SELECT Product_Name, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

--Discount Impact On Profit

SELECT Discount, AVG(Profit) AS Avg_Profit
FROM sales
GROUP BY Discount
ORDER BY Discount;

--Region-wise Sales

SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region;

--Profit Margin Insight

SELECT Category,
       SUM(Profit) * 1.0 / SUM(Sales) AS Profit_Margin
FROM sales
GROUP BY Category;








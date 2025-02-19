# Discount-Impact-Analysis
Customer Spending Behavior Analysis Report
Methodology
To analyze customer spending behavior before and after the application of discounts, we followed these steps:
1.	Data Loading and Preparation:
o	The dataset was loaded using Pandas, and display settings were adjusted for better readability.
o	The dataset was sorted by customer_id and discount_applied for structured analysis.
2.	Customer Segmentation:
o	Customers were classified into repeating customers (who made purchases more than once) and non-repeating customers (who made a single purchase).
o	This was determined by counting occurrences of each customer_id and categorizing accordingly.
3.	Order Count Analysis:
o	A function was developed to calculate the percentage of customers who increased their order count after receiving a discount.
o	The dataset was grouped by discount_applied to compare order increases among discounted and non-discounted customers.
4.	Total Spend Analysis:
o	A function was developed to compute the percentage of customers who increased their total spending after the observed period.
o	Similar to order count analysis, spending behavior was compared between discounted and non-discounted groups.
5.	Final Analysis and Reporting:
o	The results were consolidated into separate DataFrames for repeating and non-repeating customers.
o	The number of customers in each segment was recorded, along with order count and spending changes.






Results

1)Comparing customer spending behavior before and after discounts
Repeating Customers Analysis (197 Customers)
Discount Applied	% Customers with More After Orders	Count (Orders Increased)	% Customers with Higher After Spending	Count (Spending Increased)
No (108 customers)	61.11%	66	85.19%	92
Yes (89 customers)	75.28%	67	73.03%	65

Non-Repeating Customers Analysis (303 Customers)
Discount Applied	% Customers with More After Orders	Count (Orders Increased)	% Customers with Higher After Spending	Count (Spending Increased)
No (146 customers)	76.71%	112	78.77%	115
Yes (157 customers)	68.15%	107	78.98%	124


2) Customer Segments Most Responsive to Discounts
Key Findings:
•	Repeat customers receiving a discount were more likely to increase their order count (75.28%) compared to non-discounted repeat customers (61.11%).
•	However, non-discounted repeat customers had a higher total spend increase (85.19%) compared to those who received discounts (73.03%).
•	Surprisingly, non-repeating customers who did not receive discounts were more likely to increase their order count (76.71%) than those who received discounts (68.15%).
•	Spending behavior was almost identical between the two groups (78.77% vs. 78.98%).



3) Recommendations for Maximizing Revenue While Maintaining Profitability
1.	Use Discounts to Boost Order Frequency Among Repeat Customers:
o	Since repeat customers respond well to discounts in terms of order count, promotions should target this segment.
2.	Avoid Over-Discounting High-Spending Repeat Customers:
o	Since non-discounted repeat customers spent more on average, they should be incentivized with loyalty perks rather than direct discounts.
3.	Leverage Alternative Incentives for Non-Repeating Customers:
o	First-time buyers are not significantly influenced by discounts. Instead, personalized recommendations, bundles, or free shipping might be more effective.
4.	Implement Tiered Discounts:
o	Higher discounts should be reserved for customers needing an incentive, while smaller perks (e.g., free shipping) should be offered to naturally high-spending customers.
5.	Continuously Optimize Through A/B Testing:
o	Testing various promotional strategies will help refine discount effectiveness and avoid unnecessary margin reductions.
Conclusion
This analysis reveals that while discounts can effectively increase order frequency, they do not always lead to higher total spending. Non-repeating customers, in particular, show little response to discounts, making alternative incentives a better option. A targeted, segmented approach will help maximize revenue while maintaining profitability.


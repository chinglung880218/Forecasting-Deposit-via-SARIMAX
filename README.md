# Deposit Volume Forecasting for ALM Using SARIMAX: A Scenario-Based Approach
### by Jiayi Wang & Ching-Lung Hsu

---

## Overview

This project develops a robust model to forecast domestic deposit volumes under varying macroeconomic conditions, leveraging **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with Exogenous Variables). **This approach offers interpretability, scenario-specific forecasting, and insights into a bank’s financial exposure.** By incorporating key macroeconomic drivers such as GDP, Treasury rates, unemployment rates, housing prices, and CPI, the model provides a comprehensive view of how external factors influence deposit trends. Additionally, scenario-based modeling using Federal Reserve stress test scenarios ensures the forecasts align with realistic economic conditions, enhancing their applicability to strategic decision-making. The results empower treasury teams with actionable insights to optimize liquidity planning, interest rate risk management, and overall balance sheet resilience.

## Objectives
1. **Interpretability:** Analyze the correlations and influence between macroeconomic indicators (GDP, Treasury Rates, Unemployment Rate, Housing Prices, CPI) and deposit volume changes.
2. **Forecasting:** Predict deposit behaviors under Federal Reserve’s stress test scenarios to inform strategic decision-making.
3. **Exposure Analysis:** Quantify the bank’s profit/loss exposure under varying future conditions.

## Correlations

<img width="800" alt="image" src="https://github.com/chinglung880218/deposit-prediction/blob/main/figs/corr.png">

## Real Deposit Curve vs Model-based Predicted Curve

<img width="800" alt="image" src="https://github.com/chinglung880218/deposit-prediction/blob/main/figs/pred_deposit.png">

## Predicted Profit Under Four Scenarios

<img width="800" alt="image" src="https://github.com/chinglung880218/deposit-prediction/blob/main/figs/pred_profit.png">

## Key Contributions

**Scenario-Based Forecasting Framework**:  
We implemented a SARIMAX model specifically designed to predict domestic deposit volumes under diverse macroeconomic scenarios. By aligning the forecasts with Federal Reserve-inspired stress-testing frameworks, we ensured the model delivers realistic and actionable insights, directly applicable to financial risk management.

**Integration of Macroeconomic Drivers**:  
This approach incorporates key economic indicators—such as GDP, Treasury rates, unemployment rates, housing prices, and CPI—into the forecasting process. By capturing and quantifying the relationships between these variables and deposit behaviors, the model provides a transparent and interpretable foundation for strategic decision-making.

**Streamlined Data Processing and Insights**:  
We developed a robust data preprocessing pipeline, addressing challenges like missing data and selecting critical variables for analysis. Additionally, we generated insightful visualizations to uncover trends and correlations, offering a deeper understanding of deposit volume dynamics before modeling.

**Advanced Stress Testing for Risk Analysis**:  
The model simulates deposit behaviors across multiple economic scenarios, providing a clear perspective on potential risks. This enables treasury teams to assess the impact of macroeconomic volatility on the bank’s balance sheet with greater confidence.

**Practical Tools for Treasury Teams**:  
Our forecasts are tailored to support critical functions such as liquidity planning and interest rate risk management. By offering actionable insights, the model helps enhance the resilience and efficiency of treasury operations.

**Reproducibility and Transparency**:  
The notebook is fully documented, featuring clear markdown explanations, detailed code comments, and visualizations. This ensures the methodology is easy to understand, replicate, and adapt for future use cases.

### Conclusion

This project offers a practical and insightful approach for banks to navigate complex economic environments. By leveraging a combination of seasonal patterns, macroeconomic indicators, and scenario-based stress testing, the model delivers actionable forecasts tailored for strategic asset-liability management. The assumption of a fixed Loan-to-Deposit Ratio simplifies the forecasting process, focusing attention on deposit behavior and its implications for liquidity and interest rate risk management.

This analysis empowers financial institutions to:
- Anticipate deposit volume fluctuations under various macroeconomic scenarios.
- Strengthen liquidity planning by ensuring adequate funding to meet operational and regulatory requirements.
- Mitigate interest rate risk by providing a clear understanding of deposit sensitivity to economic changes.
- Enhance decision-making with a transparent, reproducible, and well-documented forecasting framework.

In conclusion, this project bridges advanced econometric modeling with practical applications, making it an invaluable tool for optimizing balance sheet strategies and ensuring financial resilience.

### Reference:

FDIC Quarterly Banking Profile: https://www.fdic.gov/quarterly-banking-profile
Dodd-Frank Act Stress Tests 2024: https://www.federalreserve.gov/supervisionreg/dfa-stress-tests-2024.htm
FRED Deposit Data: https://fred.stlouisfed.org/series/DPSACBW027SBOG#

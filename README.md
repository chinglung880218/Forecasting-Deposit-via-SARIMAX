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

## Real Deposit Curve vs Model-based Predicted Curve

## Predicted Profit Under Four Scenarios

## Key Contributions

1. **Scenario-Based Forecasting Framework**:
   - Implements a SARIMAX model to predict domestic deposit volumes under different macroeconomic scenarios.
   - Forecasts are aligned with Federal Reserve-inspired stress-testing scenarios for realistic and actionable insights.

2. **Integration of Macroeconomic Drivers**:
   - Analyzes the impact of economic indicators such as GDP, Treasury rates, unemployment rates, housing prices, and CPI on deposit volumes.
   - Provides interpretability by quantifying correlations between external factors and deposit behavior.

3. **Data Processing and Pre-modeling Insights**:
   - Includes preprocessing steps such as handling missing data and selecting key variables for modeling.
   - Visualizes trends and relationships for preliminary insights into deposit dynamics.

4. **Stress Testing for Risk Assessment**:
   - Simulates deposit behavior under multiple economic scenarios to evaluate potential risks and their impact on the bank’s balance sheet.

5. **Actionable Outputs for Treasury Teams**:
   - Provides forecasts to support liquidity planning and interest rate risk management.
   - Offers practical tools to enhance strategic resilience.

6. **Documentation and Reproducibility**:
   - Includes clear markdown explanations, code comments, and visualizations to ensure the notebook is easy to understand and replicate.

### Conclusion

This project offers a practical and insightful approach for banks to navigate complex economic environments. By leveraging a combination of seasonal patterns, macroeconomic indicators, and scenario-based stress testing, the model delivers actionable forecasts tailored for strategic asset-liability management. The assumption of a fixed Loan-to-Deposit Ratio simplifies the forecasting process, focusing attention on deposit behavior and its implications for liquidity and interest rate risk management.

This analysis empowers financial institutions to:
- Anticipate deposit volume fluctuations under various macroeconomic scenarios.
- Strengthen liquidity planning by ensuring adequate funding to meet operational and regulatory requirements.
- Mitigate interest rate risk by providing a clear understanding of deposit sensitivity to economic changes.
- Enhance decision-making with a transparent, reproducible, and well-documented forecasting framework.

In conclusion, this project bridges advanced econometric modeling with practical applications, making it an invaluable tool for optimizing balance sheet strategies and ensuring financial resilience.


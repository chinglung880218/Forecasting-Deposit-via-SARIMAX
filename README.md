# Deposit Volume Forecasting for ALM Using SARIMAX: A Scenario-Based Approach
### by Jiayi Wang & Ching-Lung Hsu

## Overview
This project focuses on forecasting deposit volumes to support Asset Liability Management (ALM) using time series techniques, specifically SARIMAX (Seasonal AutoRegressive Integrated Moving Average with exogenous factors). The project aims to provide actionable insights for managing liquidity, funding costs, and interest rate risks by leveraging historical data and macroeconomic indicators. Additionally, it incorporates scenario analysis to evaluate deposit behavior under varying economic conditions.

---

## Objectives
- Develop a robust framework to predict deposit volumes based on historical trends and macroeconomic variables.
- Explore the sensitivity of deposit levels to key macroeconomic factors (e.g., GDP, unemployment, Treasury rates).
- Simulate deposit behavior under baseline and stress scenarios to assess potential liquidity needs.
- Provide recommendations to optimize balance sheet strategies within an ALM framework.

---

## Methodology
### 1. Data Collection
- **Sources**: FDIC Quarterly Banking Profiles, Federal Reserve Economic Data (FRED), and other relevant financial datasets.
- **Scope**: Historical deposit data and macroeconomic indicators such as GDP, unemployment rate, CPI, and Treasury rates.

### 2. Exploratory Data Analysis (EDA)
- Analyze trends, seasonality, and correlations between deposits and macroeconomic variables.
- Segment deposits into categories (e.g., core vs. rate-sensitive deposits).

### 3. Forecasting Models
#### Baseline Model:
- **SARIMAX**: Predict deposit growth using time series data with exogenous macroeconomic variables.
- **Evaluation Metrics**: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE).

#### Enhanced Forecasting:
- Integrate macroeconomic indicators into SARIMAX to model deposit sensitivity to external factors.
- Test alternative methods (e.g., VAR) for comparison.

### 4. Scenario Analysis and Stress Testing
- Simulate deposit behavior under Federal Reserve stress-test scenarios (e.g., severely adverse, adverse, baseline).
- Quantify potential deposit outflows and liquidity gaps in stress conditions.

### 5. Validation
- Split data into training and testing sets for model performance evaluation.
- Back-test forecasts against historical stress events.

---

## Deliverables
1. **Forecasting Framework**:  
   - A time series model for predicting deposit volumes under baseline and stress scenarios.
2. **Scenario-Based Insights**:  
   - Analysis of deposit trends and liquidity needs under varying economic conditions.
3. **Sensitivity Analysis**:  
   - Quantification of deposit response to changes in macroeconomic variables.
4. **Visualization**:  
   - Interactive dashboards or static plots illustrating key findings.
5. **Recommendations**:  
   - Practical strategies for managing liquidity and funding within an ALM context.

---

## Tools and Skills
### Programming
- **Python**: Libraries include pandas, statsmodels, scikit-learn, matplotlib, and Plotly.

### Data Sources
- FDIC Quarterly Banking Profiles
- Federal Reserve Economic Data (FRED)

### Statistical Techniques
- SARIMAX modeling

---

## Value Proposition
This project bridges data analytics and financial decision-making by providing a comprehensive deposit forecasting model. It demonstrates practical ALM applications, equipping users with tools to analyze and respond to changes in deposit volumes under different economic scenarios.

---


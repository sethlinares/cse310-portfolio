# Overview

My data science project takes a look at the role of customer analytics within the banking sector, with a primary focus on understanding and predicting customer responses to marketing campaigns. As a software engineer, my intent is to bring together data analysis and machine learning, providing a greater look into the data at hand and creating a predictive model that can be used to forecast customer behavior. I believe that this project will serve as a stepping stone in my journey to becoming a better analyst and data scientist, as it will allow me to explore the various aspects of data science, from data wrangling and exploratory data analysis to predictive modeling and model evaluation. One of the more exciting aspects of this project is the use of neural networks to create a predictive model, as it will allow me to explore the world of deep learning and its applications in data science. With the rise of ChatGPT, Bard, and other prominent deep learning models, I feel that it is important to understand the underlying concepts and techniques that make these models so powerful, and I believe that this project has given me a chance to do so.

## Dataset Description

The dataset used in this project originates from the UCI Machine Learning Repository, specifically the [Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing). This data corresponds to direct marketing campaigns (phone calls) of a Portuguese banking institution, spanning from May 2008 to November 2010. The campaigns aimed at promoting a term deposit subscription (a fixed-term investment that yields interest over a specified period of time) to existing customers. Additionally, the dataset contains information about the customers contacted during the campaign, as well as their responses to the marketing efforts. The inclusion of this data allows for a more comprehensive analysis of the marketing campaigns, as it provides insight into the customer’s demographic and economic context, which can be used to understand their response to the campaign.

The dataset I am working with contains the following:
- **37,069 entries**
- **20 columns**: Including details about the customer (age, job, marital status), the campaign (communication type, last contact duration), and other attributes.
    - The data contains both numerical and categorical variables, each providing different kinds of information about the customers and the campaign.
- **Target Variable**: Indicates whether the client subscribed to a term deposit ('yes'/'no').

## Objectives and Purpose

The primary objective of this project is to analyze the banking dataset to gather insights into customer preferences and behaviors during the marketing campaigns. Additionally, the project aims to develop a predictive model capable of forecasting a customer’s response to future marketing campaigns. I believe that this analysis can be used to optimize marketing campaigns, as it provides a better understanding of the customer’s needs and preferences, allowing for more targeted marketing efforts. If you know what each customer wants, you can tailor your marketing efforts to meet their needs, increasing the likelihood of a successful campaign and guaranteeing a higher return on investment.

Through exploratory data analysis, I hope to answer the following questions:
- **What is the difference in term deposit status based on marital status?**
- **Does contacting people too frequently for these marketing campaigns have an adverse effect on the outcome?**
- **How do variations in economic indicators correlate with the subscription to a term deposit?**






# Video Demo


[Data Analysis Demo](https://youtu.be/-wdGPZkwYbs)





# Data Analysis Results


- **Questions**:
    - *What is the difference in term deposit status based on marital status?*
        - The data shows that single individuals are more likely to subscribe to a term deposit. This is likely due to the fact that single individuals are younger and have less financial responsibilities, allowing them to invest in a term deposit. The data also showed that divorced and married individuals are equally likely to subscribe to a term deposit, but are still about 3% less likely to subscribe than single individuals.
    - *Does contacting people too frequently for these marketing campaigns have an adverse effect on the outcome?*
        - The results of the analysis seems to indicate that contacting people too frequently for these marketing campaigns does have an adverse effect on the outcome. The data shows that the initial contact is the most effective, with the likelihood of a term deposit subscription decreasing with each subsequent contact. This seems to indicate that the more you contact a customer, the less likely they are to subscribe to a term deposit. At about 4-5 contacts, the return on investment is much lower, signaling that the bank should consider limiting the number of contacts per customer. 
    - *How do variations in economic indicators correlate with the subscription to a term deposit?*
        - While the correlations between economic indicators and subscription outcomes aren't particularly strong, there is clearly a hint of some influence from the economic context on subscription outcomes. For instance, the negative correlations between `emp.var.rate`, `euribor3m`, and subscription outcomes imply that as these indicators rise, the likelihood of clients subscribing to term deposits reduces, potentially signaling greater financial caution or different investment strategies among clients during these economic periods. This implies that the bank should consider the economic situation when crafting client engagement strategies, as it could influence client behavior and decisions. For instance, during periods of economic uncertainty, clients might be more cautious and less likely to subscribe to term deposits, which could be a factor to consider.

- **Predictive Model**:
    - *Model Architecture*
        - The model used is called a `Deep Neural Network (DNN)`, which is a type of neural network that contains multiple hidden layers. The model consists of many hidden layers, each containing hundreds or thousands of neurons.
    - *Model Performance*
        - The model achieved an accuracy of 90.5% on the test set, which is a fairly good result. This means that the model was able to correctly predict the outcome of 90.5% of the test data. Despite the high accuracy, the model still has trouble predicting the minority class, which is the `yes` class. This is due to the fact that the dataset is heavily imbalanced, with the `no` class having significantly more data than the `yes` class. This imbalance causes the model to be biased towards the majority class, making the model amazing at predicting who does not want to subscribe, but terrible at predicting who does want to subscribe. This is a problem that needs to be addressed at the data level, as the model cannot be expected to perform well when the data is imbalanced. While oversampling the `yes` class can improve the model's ability to predict the minority class, it is not a perfect solution, as it drastically reduces the performance of the model on the majority class. This is a trade-off that needs to be considered when dealing with imbalanced data. Ultimately, I decided against oversampling the data, as I felt that the model's ability to predict who does not want to subscribe is extremely important, as it allows the bank to focus their marketing efforts on those who are more likely to subscribe, increasing the likelihood of a successful campaign and guaranteeing a higher return on investment.

# Development Environment

{Describe the tools that you used to develop the software}

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, TensorFlow, Keras
- **IDE**: Visual Studio Code



# Useful Websites

* [MIT Introduction to Deep Learning](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLTZ1bhP8GBuTCqeY19TxhHyrwFiot42_U)
* [Panda's Documentation](https://pandas.pydata.org/docs/user_guide/index.html)
* [Deep Learning: Feed Forward Neural Networks](https://medium.com/@b.terryjack/introduction-to-deep-learning-feed-forward-neural-networks-ffnns-a-k-a-c688d83a309d)


# Future Work

* Improve the model's ability to predict the minority class.
* Explore other deep learning models, such as Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs).
* Incorporate other data sources to improve the model's predictive power.
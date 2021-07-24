# Deep Learning Macroeconomics

Deep learning has achieved state-of-the-art success in recognizing patterns. Since there are patterns to be recognized in economics, in this work, deep learning is applied to macroeconomics in two approaches: to transfer learning and to interpolate, distribute, and extrapolate time series by related series.

Transfer learning is proposed as an additional strategy for empirical macroeconomics. When developing economics modeling strategies, the lack of data may be an issue that transfer learn- ing can fix. First, we present theoretical concepts related to transfer learning and proposed a connection with a typology related to macroeconomic models. Secondly, we explore the proposed strategy empirically, showing that data from different but related domains, a type of transfer learn- ing, helps identify the business cycle phases when there is no business cycle dating committee and to quick estimate a economic-based output gap. In both cases, the proposed strategy also helps to improve the learning when data is limited. The approach integrates the idea of storing knowledge gained from one region’s economics experts and applying it to other geographic areas. The first is captured with a supervised deep neural network model, and the second by applying it to another dataset, a domain adaptation procedure. Overall, there is an improvement in the classification with transfer learning compared to baseline models. The results, based on the United States, the selected Europe countries and the Brazilian datasets, indicate that the method proposed leads to successful business cycle identification and output gap estimation. To the best of our knowledge, the combined deep and transfer learning approach is underused for application to macroeconomic problems, indicating that there is plenty of room for research development.

Additionally, since deep learning methods are a way of learning representations, those that are formed by the composition of multiple non-linear transformations, to yield more abstract representations, we apply deep learning for mapping low-frequency from high-frequency variables, a task also known as interpolation, distribution, and extrapolation of time series by related series. The results obtained from Brazilian data demonstrate deep learning’s suitability for this task.

## TL4BC folder
Codes and files: Chapter - Transfer Learning for Business Cycle

## TL4OG folder
Codes and files: Chapter - Transfer Learning for Output Gap 

## RIDE browser-based model with tensorflow.js - www.deeplearningeconomics.com/RIDE

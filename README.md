# Deep Learning Macroeconomics

Limited datasets and complex nonlinear relationships are among the challenges that may emerge when applying econometrics to macroeconomic problems. This research proposes deep learning as an approach to transfer learning in the former case and to map relationships between variables in the latter case. Several machine learning techniques are incorporated into the econometric framework, but deep learning remains focused on time-series forecasting. The approach proposed here is also related to pattern recognition, but where deep learning has achieved state-ofthe-art performance: progressively using multiple layers to extract higher-level features from the raw input.

Firstly, transfer learning is proposed as an additional strategy for empirical macroeconomics. Although macroeconomists already apply transfer learning when assuming a given a priori distribution in a Bayesian context, estimating a structural VAR with signal restriction and calibrating parameters based on results observed in other models, to name a few examples, advance in a more systematic transfer learning strategy in applied macroeconomics is the innovation we are introducing. When developing economics modeling strategies, the lack of data may be an issue that transfer learning can fix. We start presenting theoretical concepts related to transfer learning and proposed a connection with a typology related to macroeconomic models. Next, we explore the proposed strategy empirically, showing that data from different but related domains, a type of transfer learning, helps identify the business cycle phases when there is no business cycle dating committee and to quick estimate a economic-based output gap. In both cases, the strategy also helps to improve the learning when data is limited. The approach integrates the idea of storing knowledge gained from one region’s economics experts and applying it to other geographic areas. The first is captured with a supervised deep neural network model, and the second by applying it to another dataset, a domain adaptation procedure. Overall, there is an improvement in the classification with transfer learning compared to baseline models. To the best of our knowledge, the combined deep and transfer learning approach is underused for application to macroeconomic problems, indicating that there is plenty of room for research development.

Secondly, since deep learning methods are a way of learning representations, those that are formed by the composition of multiple non-linear transformations, to yield more abstract representations, we apply deep learning for mapping low-frequency from high-frequency variables. There are situations where we know, sometimes by construction, that there is a relationship between input and output variables, but this relationship is difficult to map, a challenge in which deep learning models have shown excellent performance.

The results obtained show the suitability of deep learning models applied to macroeconomic problems. First, models learned to classify United States business cycles correctly. Then, applying transfer learning, they were able to identify the business cycles of out-of-sample Brazilian and European data. Along the same lines, the models learned to estimate the output gap based on the U.S. data and obtained good performance when faced with Brazilian data. In both cases, the proposed strategy emerges as a potential supplementary tool for governments and the private sector to conduct their activities in the light of national and international economic conditions. Additionally, deep learning proved adequate for mapping low-frequency variables from high-frequency data to interpolate, distribute, and extrapolate time series by related series. The application of this technique to Brazilian data proved to be compatible with benchmarks based on other techniques.

## arXiv BibTex Citation
@misc{guimaraes2022deep,
      title={Deep Learning Macroeconomics}, 
      author={Rafael R. S. Guimaraes},
      year={2022},
      eprint={2201.13380},
      archivePrefix={arXiv},
      primaryClass={econ.EM}
}

## TL4BC folder
Codes and files: Chapter - Transfer Learning for Business Cycle

## TL4OG folder
Codes and files: Chapter - Transfer Learning for Output Gap 

## RIDE browser-based model 
www.deeplearningeconomics.com/RIDE: Chapter - Representation Learning for Interpolation, Distribution and Extrapolation of time series by related series

## YouTube channel
https://www.youtube.com/channel/UCtDACYNXs4BUjGf4Com-0SQ

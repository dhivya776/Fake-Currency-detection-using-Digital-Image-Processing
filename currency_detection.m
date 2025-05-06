% Fake Currency Detection Project

% 1. Image Preprocessing
originalCurrency = imread("D:\DIP-Project\original note.jpg");
currencyTemplate = imread("D:\DIP-Project\ake note.jpg");

originalGray = rgb2gray(originalCurrency);
templateGray = rgb2gray(currencyTemplate);

% 2. Feature Extraction
% Detect keypoints using SURF
points = detectSURFFeatures(originalGray);

% Extract features using the detected keypoints
originalFeatures = extractFeatures(originalGray, points);

% Detect keypoints using SURF
points = detectSURFFeatures(templateGray);

% Extract features using the detected keypoints
templateFeatures = extractFeatures(originalGray, points);


% 3. Classification
classifier = fitcecoc(originalFeatures, labels);
predictedLabels = predict(classifier, templateFeatures);

% 4. Result Visualization
subplot(1, 2, 1);
imshow(originalCurrency);
title('Original Currency');

subplot(1, 2, 2);
imshow(currencyTemplate);
title('Currency Template');

if predictedLabels == 1
    disp('Result: Original Currency');
else
    disp('Result: Fake Currency');
end

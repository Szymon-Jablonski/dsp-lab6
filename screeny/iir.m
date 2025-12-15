close all;
clear all;

fs = 50000; % sampling frequency
[b a] = butter(1, [500, 2000]/(fs/2)); % bandpass

freqz(b, a, 1024);

fprintf("bCoeff = {");
fprintf('%.6ff, ', b);
fprintf('}\n');

fprintf("aCoeff = {");
fprintf('%.6ff, ', a);
fprintf('}');
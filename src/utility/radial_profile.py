import numpy as np
from typing import Dict

ECE_channel_mapping = {
    "\\ECE01":[1.369,1.461,1.552,1.643,1.734,1.826,1.917,2.008,2.100,2.191,2.282,0,0,0,0,0],
    '\\ECE02':[1.357,1.447,1.538,1.628,1.719,1.809,1.900,1.990,2.081,2.171,2.262,0,0,0,0,0],
    '\\ECE03':[1.345,1.435,1.524,1.614,1.704,1.793,1.883,1.972,2.062,2.152,2.241,0,0,0,0,0],
    '\\ECE04':[1.333,1.422,1.511,1.600,1.688,1.777,1.866,1.955,2.044,2.133,2.222,2.310,0,0,0,0],
    '\\ECE05':[1.321,1.409,1.497,1.586,1.674,1.762,1.850,1.938,2.026,2.114,2.202,2.290,0,0,0,0],
    '\\ECE06':[1.310,1.397,1.484,1.572,1.659,1.746,1.834,1.921,2.008,2.096,2.183,2.270,0,0,0,0],
    '\\ECE07':[1.299,1.385,1.472,1.558,1.645,1.731,1.818,1.904,1.991,2.078,2.164,2.251,0,0,0,0],
    '\\ECE08':[1.287,1.373,1.459,1.545,1.631,1.717,1.802,1.888,1.974,2.060,2.146,2.231,0,0,0,0],
    '\\ECE09':[1.276,1.362,1.447,1.532,1.617,1.702,1.787,1.872,1.957,2.042,2.127,2.213,2.298,0,0,0],
    '\\ECE10':[1.266,1.350,1.435,1.519,1.603,1.688,1.772,1.856,1.941,2.025,2.110,2.194,2.278,0,0,0],
    '\\ECE11':[0,1.339,1.423,1.506,1.590,1.674,1.757,1.841,1.925,2.008,2.092,2.176,2.259,0,0,0],
    '\\ECE12':[0,1.328,1.411,1.494,1.577,1.660,1.743,1.826,1.909,1.992,2.075,2.158,2.241,0,0,0],
    '\\ECE13':[0,1.306,1.388,1.470,1.551,1.633,1.714,1.796,1.878,1.959,2.041,2.123,2.204,2.286,0,0],
    '\\ECE14':[0,1.296,1.377,1.458,1.539,1.620,1.701,1.782,1.863,1.944,2.025,2.106,2.187,2.267,0,0],
    '\\ECE15':[0,1.285,1.366,1.446,1.526,1.607,1.687,1.767,1.848,1.928,2.008,2.089,2.169,2.249,0,0],
    '\\ECE16':[0,1.275,1.355,1.435,1.514,1.594,1.674,1.753,1.833,1.913,1.992,2.072,2.152,2.231,2.311,0],
    '\\ECE17':[0,1.265,1.344,1.423,1.502,1.581,1.660,1.740,1.819,1.898,1.977,2.056,2.135,2.214,2.293,0],
    '\\ECE18':[0,0,1.334,1.412,1.491,1.569,1.647,1.726,1.804,1.883,1.961,2.040,2.118,2.197,2.275,0],
    '\\ECE19':[0,0,1.323,1.401,1.479,1.557,1.635,1.713,1.790,1.868,1.946,2.024,2.102,2.18,2.257,0],
    '\\ECE20':[0,0,1.313,1.390,1.468,1.545,1.622,1.699,1.777,1.854,1.931,2.008,2.086,2.163,2.24,0],
    '\\ECE21':[0,0,1.303,1.380,1.456,1.533,1.610,1.686,1.763,1.840,1.916,1.993,2.070,2.146,2.223,2.300],
    '\\ECE22':[0,0,1.293,1.369,1.445,1.521,1.598,1.674,1.750,1.826,1.902,1.978,2.054,2.13,2.206,2.282],
    '\\ECE23':[0,0,1.284,1.359,1.435,1.510,1.586,1.661,1.737,1.812,1.888,1.963,2.039,2.114,2.19,2.265],
    '\\ECE24':[0,0,1.274,1.349,1.424,1.499,1.574,1.649,1.724,1.799,1.873,1.948,2.023,2.098,2.173,2.248],
    '\\ECE25':[0,0,0,1.310,1.383,1.455,1.528,1.601,1.674,1.746,1.819,1.892,1.965,2.037,2.11,2.183],
    '\\ECE26':[0,0,0,1.300,1.373,1.445,1.517,1.589,1.662,1.734,1.806,1.878,1.951,2.023,2.095,2.167],
    '\\ECE27':[0,0,0,1.291,1.363,1.435,1.506,1.578,1.650,1.721,1.793,1.865,1.937,2.008,2.08,2.152],
    '\\ECE28':[0,0,0,1.282,1.353,1.424,1.496,1.567,1.638,1.709,1.780,1.852,1.923,1.994,2.065,2.137],
    '\\ECE29':[0,0,0,1.273,1.344,1.414,1.485,1.556,1.626,1.697,1.768,1.839,1.909,1.98,2.051,2.121],
    '\\ECE30':[0,0,0,1.264,1.334,1.404,1.475,1.545,1.615,1.685,1.756,1.826,1.896,1.966,2.036,2.107],
    '\\ECE31':[0,0,0,0,1.325,1.395,1.464,1.534,1.604,1.674,1.743,1.813,1.883,1.953,2.022,2.092],
    '\\ECE32':[0,0,0,0,1.316,1.385,1.454,1.524,1.593,1.662,1.731,1.801,1.870,1.939,2.008,2.078],
    '\\ECE33':[0,0,0,0,1.307,1.376,1.444,1.513,1.582,1.651,1.719,1.788,1.857,1.926,1.995,2.063],
    '\\ECE34':[0,0,0,0,1.298,1.366,1.435,1.503,1.571,1.639,1.708,1.776,1.844,1.913,1.981,2.049],
    '\\ECE35':[0,0,0,0,1.289,1.357,1.425,1.493,1.561,1.628,1.696,1.764,1.832,1.9,1.968,2.035],
    '\\ECE36':[0,0,0,0,1.280,1.348,1.415,1.483,1.550,1.617,1.685,1.752,1.820,1.887,1.954,2.022],
    '\\ECE37':[0,0,0,0,1.264,1.330,1.397,1.463,1.530,1.596,1.663,1.729,1.796,1.862,1.929,1.995],
    '\\ECE38':[0,0,0,0,0,1.321,1.387,1.453,1.519,1.586,1.652,1.718,1.784,1.85,1.916,1.982],
    '\\ECE39':[0,0,0,0,0,1.313,1.378,1.444,1.510,1.575,1.641,1.706,1.772,1.838,1.903,1.969],
    '\\ECE40':[0,0,0,0,0,1.304,1.369,1.435,1.500,1.565,1.630,1.695,1.761,1.826,1.891,1.956],
    '\\ECE41':[0,0,0,0,0,1.296,1.360,1.425,1.490,1.555,1.620,1.684,1.749,1.814,1.879,1.944],
    '\\ECE42':[0,0,0,0,0,1.287,1.352,1.416,1.481,1.545,1.609,1.674,1.738,1.802,1.867,1.931],
    '\\ECE43':[0,0,0,0,0,1.279,1.343,1.407,1.471,1.535,1.599,1.663,1.727,1.791,1.855,1.919],
    '\\ECE44':[0,0,0,0,0,1.271,1.335,1.398,1.462,1.525,1.589,1.652,1.716,1.78,1.843,1.907],
    '\\ECE45':[0,0,0,0,0,1.263,1.326,1.389,1.453,1.516,1.579,1.642,1.705,1.768,1.832,1.895],
    '\\ECE46':[0,0,0,0,0,0,1.318,1.381,1.444,1.506,1.569,1.632,1.695,1.757,1.82,1.883],
    '\\ECE47':[0,0,0,0,0,0,1.310,1.372,1.435,1.497,1.559,1.622,1.684,1.746,1.809,1.871],
    '\\ECE48':[0,0,0,0,0,0,1.302,1.364,1.426,1.488,1.550,1.612,1.674,1.736,1.798,1.860],
    '\\ECE49':[1.931,2.060,2.189,0,0,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE50':[1.907,2.034,2.161,2.288,0,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE51':[1.860,1.984,2.108,2.231,0,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE52':[1.837,1.959,2.082,2.204,0,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE53':[1.815,1.936,2.057,2.178,2.299,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE54':[1.793,1.913,2.032,2.152,2.271,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE55':[1.772,1.890,2.008,2.126,2.245,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE56':[1.751,1.868,1.985,2.102,2.219,0,0,0,0,0,0,0,0,0,0,0],
    '\\ECE57':[1.731,1.847,1.962,2.078,2.193,2.308,0,0,0,0,0,0,0,0,0,0],
    '\\ECE58':[1.712,1.826,1.940,2.054,2.168,2.282,0,0,0,0,0,0,0,0,0,0],
    '\\ECE59':[1.692,1.805,1.918,2.031,2.144,2.257,0,0,0,0,0,0,0,0,0,0],
    '\\ECE60':[1.674,1.785,1.897,2.008,2.120,2.231,0,0,0,0,0,0,0,0,0,0],
    '\\ECE61':[1.655,1.766,1.876,1.986,2.097,2.207,0,0,0,0,0,0,0,0,0,0],
    '\\ECE62':[1.637,1.746,1.856,1.965,2.074,2.183,2.292,0,0,0,0,0,0,0,0,0],
    '\\ECE63':[1.569,1.674,1.778,1.883,1.987,2.092,2.197,2.301,0,0,0,0,0,0,0,0],
    '\\ECE64':[1.553,1.656,1.760,1.863,1.967,2.070,2.174,2.278,0,0,0,0,0,0,0,0],
    '\\ECE65':[1.537,1.639,1.742,1.844,1.947,2.049,2.152,2.254,0,0,0,0,0,0,0,0],
    '\\ECE66':[1.521,1.623,1.724,1.826,1.927,2.029,2.130,2.231,0,0,0,0,0,0,0,0],
    '\\ECE67':[1.506,1.607,1.707,1.808,1.908,2.008,2.109,2.209,2.310,0,0,0,0,0,0,0],
    '\\ECE68':[1.491,1.591,1.690,1.790,1.889,1.988,2.088,2.187,2.287,0,0,0,0,0,0,0],
    '\\ECE69':[1.477,1.575,1.674,1.772,1.871,1.969,2.067,2.166,2.264,0,0,0,0,0,0,0],
    '\\ECE70':[1.462,1.560,1.657,1.755,1.852,1.950,2.047,2.145,2.242,0,0,0,0,0,0,0],
    '\\ECE71':[1.448,1.545,1.641,1.738,1.835,1.931,2.028,2.124,2.221,0,0,0,0,0,0,0],
    '\\ECE72':[1.435,1.530,1.626,1.721,1.817,1.913,2.008,2.104,2.200,2.295,0,0,0,0,0,0],
    '\\ECE73':[1.421,1.516,1.610,1.705,1.800,1.895,1.989,2.084,2.179,2.274,0,0,0,0,0,0],
    '\\ECE74':[1.408,1.502,1.595,1.689,1.783,1.877,1.971,2.065,2.159,2.252,0,0,0,0,0,0],
    '\\ECE75':[1.382,1.474,1.566,1.658,1.750,1.843,1.935,2.027,2.119,2.211,2.303,0,0,0,0,0],
    '\\ECE76':[1.369,1.461,1.552,1.643,1.734,1.826,1.917,2.008,2.100,2.191,2.282,0,0,0,0,0],
}

TCI_channel_mapping = {
    '\\ne_tci01':1.34,
    '\\ne_tci02':1.78,
    '\\ne_tci03':1.91,
    '\\ne_tci04':2.04,
    '\\ne_tci05':2.16,
}

class ECEprofileMapper:
    def __init__(self):
        self.B_list = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0],
        self.mapping = ECE_channel_mapping
        
    def __call__(self, ECE_inputs:Dict, B:float):
        idx_match = self._match_B(B)
        
        ECE_1D_profile = {}        
        
        for channel in ECE_inputs.keys():
            rpos = self.mapping[channel][idx_match]
            ECE_1D_profile[channel] = [rpos, ECE_inputs[channel]]
            
        return ECE_1D_profile
    
    def _match_B(self, B:float):
        db = np.array([abs(b-B) for b in self.B_list])
        idx = np.argmin(db)
        return idx

import sys
from hrvanalysis import remove_outliers, remove_ectopic_beats, interpolate_nan_values, get_time_domain_features, \
    get_frequency_domain_features, get_geometrical_features, get_csi_cvi_features, get_poincare_plot_features, plot_psd, \
    plot_poincare, plot_distrib, plot_timeseries, get_sampen, get_nn_intervals
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def to_rr_milliseconds(x):
    return int(x * 1000)


@app.route('/hrv-analysis')
def hrv():
    hr_list = [float(c) for c in request.args.get('list').split(',')]
    rr_intervals_list = list(map(to_rr_milliseconds, hr_list))
    interpolated_nn_intervals = get_nn_intervals(rr_intervals_list, ectopic_beats_removal_method="malik")
    time_domain_features = get_time_domain_features(interpolated_nn_intervals).__str__()
    freq_domain_features = get_frequency_domain_features(interpolated_nn_intervals).__str__()
    geo_domain_features = get_geometrical_features(interpolated_nn_intervals).__str__()
    csi_domain_features = get_csi_cvi_features(interpolated_nn_intervals).__str__()
    samp_en_domain_features = get_sampen(interpolated_nn_intervals).__str__()
    poincare = get_poincare_plot_features(interpolated_nn_intervals).__str__()
    non_linear_domain_features = '{%s,%s,%s}' % (
        poincare.replace('{', '').replace('}', ''), csi_domain_features.replace('{', '').replace('}', ''),
        samp_en_domain_features.replace('{', '').replace('}', ''))
    return jsonify({'time_domain_features': time_domain_features, 'freq_domain_features': freq_domain_features,
                    'geo_domain_features': geo_domain_features,
                    'non_linear_domain_features': non_linear_domain_features,
                    'total_items': len(rr_intervals_list),
                    'interpolated_intervals': len(interpolated_nn_intervals)})


if __name__ == '__main__':
    app.run()

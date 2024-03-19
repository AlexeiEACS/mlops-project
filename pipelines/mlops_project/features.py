import pandas as pd
import os
import sys
# Encoders of data
week_day_encoder = {'Weekday': 0,
                    'Weekend': 1}
day_week_encoder = {'Monday': 0,
                    'Tuesday': 1,
                    'Wednesday': 2,
                    'Thursday': 3,
                    'Friday': 4,
                    'Saturday': 5,
                    'Sunday': 6}
load_type_encoder = {'Light_Load': 0,
                     'Medium_Load': 1,
                     'Maximum_Load': 2}

# Final schema of DataFrame
data_types = {'date',
              'Usage_kWh',
              'Leading_Current_Reactive_Power_kVarh',
              'CO2(tCO2)',
              'Lagging_Current_Power_Factor',
              'Leading_Current_Power_Factor',
              'NSM',
              'WeekStatus',
              'Day_of_week',
              'Load_Type',
              'hours',
              'week_day_coded',
              'day_week_encoder',
              'loadtype_encoder'
              }


def encode_categorical_data(data):
    try:
        data['week_day_coded'] = data.WeekStatus.map(week_day_encoder)
        data['day_week_encoder'] = data.Day_of_week.map(day_week_encoder)
        data['loadtype_encoder'] = data.Load_Type.map(load_type_encoder)
        log_info("Encoded categorical data")
        return data
    except Exception as exp:
        log_error(exp)


def final_out(data):
    try:
        data["date"] = pd.to_datetime(data["date"], format="%d/%m/%Y %H:%M")
        data["hours"] = data["date"].dt.hour
        data.drop('Lagging_Current_Reactive.Power_kVarh', axis=1, inplace=True)
        log_info("Finished out data")
    except Exception as exp:
        log_error(exp)


if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..')))
    from config.logger import log_info, log_error

    path_procesed = "data/1_interim/procesed_data.csv"

    data_path = os.path('data/0_raw/Steel_industry_data.csv')
    data = pd.read_csv(data_path)

    data_encoded = encode_categorical_data(data)
    final_procesed_data = final_out(data_encoded)
    final_procesed_data.to_csv(path_procesed)

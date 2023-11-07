SELECT festival, date(actual_start_date + INTERVAL '-7 day') as departure_dates, date(actual_start_date + INTERVAL '-7 day' + INTERVAL '1 month') as arrival_dates
FROM public.indian_festivals
WHERE actual_start_date - current_date >= 30 AND actual_start_date - current_date <= 60;
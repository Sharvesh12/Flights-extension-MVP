SELECT festival, date(start_date + INTERVAL '-7 day') as departure_dates, date(start_date + INTERVAL '-7 day' + INTERVAL '1 month') as arrival_dates
FROM public.indian_holidays
WHERE start_date - current_date >= 45 AND start_date - current_date <= 60;
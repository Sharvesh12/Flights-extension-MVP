SELECT festival, start_date + INTERVAL '-7 day' as departure_dates, start_date + INTERVAL '-7 day' + INTERVAL '1 month' as arrival_dates
FROM public.indian_holidays
WHERE start_date - current_date >= 30 AND start_date - current_date <= 90
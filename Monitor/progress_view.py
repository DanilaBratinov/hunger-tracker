def get_progress_view(mode, hour, minutes):
    current = mode * 60
    interval = hour * 60 + minutes
    result = round(interval / current * 100, 2)

    progress = round(result / 5)
    progress_view = [""]

    def get_progress(symbol, count):
        for number in range(0, count):
            progress_view.append(f"{symbol}")
        full_view = ''.join(progress_view)

        return full_view

    get_progress('#', progress)
    remainder = 20 - (len(progress_view) - 1)
    progress_final = get_progress(' ', remainder)

    return (f"Голодание завершено на: \n[{progress_final}]     {result}%")



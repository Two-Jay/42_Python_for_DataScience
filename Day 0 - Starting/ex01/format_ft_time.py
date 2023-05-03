import datetime

def get_raw_time() -> float:
    return datetime.datetime.timestamp(datetime.datetime.now())

def get_formatted_time() -> datetime.datetime:
    return datetime.datetime.now()

def print_time(raw_time : float, formatted_time : datetime.datetime) -> None:
    print(f"Seconds since January 1, 1970: {raw_time:,.4f} or {raw_time:.2e} in scientific notation")
    print(f"{get_formatted_time().strftime('%B %d %Y')}")

if __name__ == "__main__":
    print_time(get_raw_time(), get_formatted_time())

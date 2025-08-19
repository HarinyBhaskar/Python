def book_trip(passenger_name, *places, **details):
    print(f"\nTravel Itinerary for {passenger_name}")
    print("-" * 35)
    print("Destinations:")
    for p in places:   # iterating through tuple of destinations
        print(f"- {p}")

    mode = details.get("mode", "Bus")        # default is Bus
    base_price = details.get("price", 1000)  # default is 1000
    discount = details.get("discount", 0)    # default is 0
    guide = details.get("guide", False)      # default is False

    final_price = base_price - discount
    if guide:
        final_price += 500  # add extra charge if guide is True

    print(f"Mode of Travel : {mode}")
    print(f"Final Price    : ₹{final_price}")
    print("-" * 35)

book_trip(
    "Ramesh",
    "Delhi", "Agra", "Jaipur",
    mode="Train", price=3500, discount=500, guide=True
)

book_trip(
    "Priya",
    "Goa", "Mumbai",
    mode="Flight", price=7000
)

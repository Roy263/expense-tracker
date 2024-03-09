def getData(year):
    return [
        {
            "$sort": {
                "created_at": 1
            }
        },
        {
            "$match": {
                "year": year,
            }
        },
        {
            "$group": {
                "_id": {"month": "$month", "year": "$year"},
                "Income": {"$sum": {"$arrayElemAt": ["$Income.amount", 0]}},
                "Tax": {"$sum": {"$arrayElemAt": ["$Tax.amount", 0]}},
                "Cash": {"$sum": {"$arrayElemAt": ["$Cash.amount", 0]}},
                "Home": {"$sum": {"$sum": "$Home.amount"}},
                "Desires": {"$sum": {"$sum": "$Desires.amount"}},
                "Credit_Card": {"$sum": {"$sum": "$Credit_Card.amount"}},
                "Investment": {"$sum": {"$sum": "$Investment.amount"}},
            }
        },
        {
            "$project": {
                "_id": 0,
                "month": "$_id.month",
                "year": "$_id.year",
                "Income": 1,
                "Tax": 1,
                "Cash": 1,
                "Home": 1,
                "Desires": 1,
                "Credit_Card": 1,
                "Investment": 1,
                "created_at": 1
            }
        },
        
    ]

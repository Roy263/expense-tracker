def getQuery(year):
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
                "_id": {"month": "$month", "year": "$year", "created_at":"$created_at"},
                "Income": {"$sum": {"$sum": "$Income.amount"}},
                "Tax": {"$sum": {"$sum": "$Tax.amount"}},
                "Cash": {"$sum": {"$sum": "$Cash.amount"}},
                "Home": {"$sum": {"$sum": "$Home.amount"}},
                "Desires": {"$sum": {"$sum": "$Desires.amount"}},
                "Travel": {"$sum": {"$sum": "$Travel.amount"}},
                "Food": {"$sum": {"$sum": "$Food.amount"}},
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
                "Travel": 1,
                "Food": 1,
                "Credit_Card": 1,
                "Investment": 1,
                "created_at": "$_id.created_at"
            }
        },
        
    ]

def getQuery(year):
    # return [
    #     {
    #         "$sort": {
    #             "created_at": 1
    #         }
    #     },
    #     {
    #         "$match": {
    #             "year": year,
    #         }
    #     },
    #     {
    #         "$group": {
    #             "_id": {"month": "$month", "year": "$year", "created_at":"$created_at"},
    #             "Income": {"$sum": {"$sum": "$Income.amount"}},
    #             "Tax": {"$sum": {"$sum": "$Tax.amount"}},
    #             "Cash": {"$sum": {"$sum": "$Cash.amount"}},
    #             "Home": {"$sum": {"$sum": "$Home.amount"}},
    #             "Desires": {"$sum": {"$sum": "$Desires.amount"}},
    #             "Travel": {"$sum": {"$sum": "$Travel.amount"}},
    #             "Food": {"$sum": {"$sum": "$Food.amount"}},
    #             "Credit_Card": {"$sum": {"$sum": "$Credit_Card.amount"}},
    #             "Investment": {"$sum": {"$sum": "$Investment.amount"}},
    #         }
    #     },
    #     {
    #         "$project": {
    #             "_id": 0,
    #             "month": "$_id.month",
    #             "year": "$_id.year",
    #             "Income": 1,
    #             "Tax": 1,
    #             "Cash": 1,
    #             "Home": 1,
    #             "Desires": 1,
    #             "Travel": 1,
    #             "Food": 1,
    #             "Credit_Card": 1,
    #             "Investment": 1,
    #             "created_at": "$_id.created_at"
    #         }
    #     },

    # ]

    return [
        {"$sort": {"created_at": -1}},
        {"$match": {"year": year}},
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
                "transactions": {
                    "$push": {
                        "Income": {"$concat": [{"$toString": {"$sum": "$Income.amount"}}, ": ", {"$arrayElemAt": ["$Income.description", 0]}]},
                        "Tax": {"$concat": [{"$toString": {"$sum": "$Tax.amount"}}, ": ", {"$arrayElemAt": ["$Tax.description", 0]}]},
                        "Cash": {"$concat": [{"$toString": {"$sum": "$Cash.amount"}}, ": ", {"$arrayElemAt": ["$Cash.description", 0]}]},
                        "Home": {"$concat": [{"$toString": {"$sum": "$Home.amount"}}, ": ", {"$arrayElemAt": ["$Home.description", 0]}]},
                        "Desires": {"$concat": [{"$toString": {"$sum": "$Desires.amount"}}, ": ", {"$arrayElemAt": ["$Desires.description", 0]}]},
                        "Travel": {"$concat": [{"$toString": {"$sum": "$Travel.amount"}}, ": ", {"$arrayElemAt": ["$Travel.description", 0]}]},
                        "Food": {"$concat": [{"$toString": {"$sum": "$Food.amount"}}, ": ", {"$arrayElemAt": ["$Food.description", 0]}]},
                        "Credit_Card": {"$concat": [{"$toString": {"$sum": "$Credit_Card.amount"}}, ": ", {"$arrayElemAt": ["$Credit_Card.description", 0]}]},
                        "Investment": {"$concat": [{"$toString": {"$sum": "$Investment.amount"}}, ": ", {"$arrayElemAt": ["$Investment.description", 0]}]}
                    }
                },
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
                "transactions": {"$slice": ["$transactions", 5]},
                "created_at": "$_id.created_at"
            }
        },
    ]

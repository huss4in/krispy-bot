SURVEY_DATA = {
    "survey": {
        "language": [
            "//form/div/ul/li/a[@href='Index.aspx?LanguageID=US']"
        ],
        "content": "//*/div[@id='middle']/div[@id='content']",
        "next": [
            "//*[@id='NextButton']",
            "//form/div/div/input[@type='submit']"
        ],
        "error": [
            "//*[@id='FNSErrorFocus']"
        ],
    },
    "receipt": {
        "page": [
            "//input[@id='CN1']"
        ],
        "questions": {
            "number": [
                "//p//label[@for='CN1']"
            ],
            "date": [
                "//p//label[@for='Index_VisitDatecontainer']"
            ],
            "time": [
                "//p//label[@for='InputHour']"
            ]
        },
        "answers": {
            "number": {
                "input": [
                    "//input[@id='CN1']",
                    "//input[@maxlength='5']",
                    "//form/div/p[4]/input"
                ]
            },
            "date": {
                "input": [
                    "//input[@id='Index_VisitDateDatePicker']",
                    "//form/div/p/span/span/input"
                ],
                "month": [
                    "//span[@class='ui-datepicker-month']",
                    "//div[2]/div/div/span[1]"
                ],
                "year": [
                    "//span[@class='ui-datepicker-year']",
                    "//div[2]/div/div/span[2]"
                ],
                "day": [
                    "//table/tbody/tr/td/a"
                ],
                "prev": [
                    "//span[@class='ui-icon ui-icon-circle-triangle-w']",
                    "//div[2]/div/a[1]/span"
                ]
            },
            "time": {
                "hour": [
                    "//select[@id='InputHour']",
                    "//select[@title='Hour']",
                    "//form/div/p/span/select[1]"
                ],
                "minute": [
                    "//select[@id='InputMinute']",
                    "//select[@title='Minute']",
                    "//form/div/p/span/select[2]"
                ],
                "meridian": [
                    "//select[@id='InputMeridian']",
                    "//select[@title='Meridiem']",
                    "//form/div/p/span/select[3]"
                ]
            }
        }
    },
    "choose": {
        "page": [
            "//form//div//div/span/span[@class='radioSimpleInput']",
            "//form//div//div/span/span[@class='checkboxSimpleInput']"
        ],
        "question": [
            "//form//div//div[@class='FNSText' and @id]",
            "//form//div//div[@class and @id]",
            "//form//div//div[@id]",
            "//form//div//div[@class='FNSText blocktitle']/span",
            "//form//div//div/label"
        ],
        "answer": [
            "//form//div//div[@class]/label"
        ]
    },
    "rate": {
        "page": [
            "//form//table/tbody/tr[1]/td[@id and @class][2]",
            "//form//table/tbody/tr[1]/td[3]"
        ],
        "questions": [
            "//table/tbody/tr[@id and @class]/td[@id]",
            "//table/tbody/tr[@id and @class]/td[1]"
        ],
        "answers": "//table/tbody/tr[@id and @class][#QUESTION#]/td[#ANSWER#]/span[@style]"
    },
    "note": {
        "page": [
            "//form//div//div/textarea",
        ],
        "question": [
            "//form//div//div/label"
        ],
        "answer": [
            "//form//div//div/textarea"
        ]
    },
    "redeem": {
        "page": [
            "//form/div//div/p[@class='FinishHeader']",
            "//form/div//div/p[@class='ValCode']"
        ]
    },
    "code": [
        "//p[@class='ValCode']"
    ]
}

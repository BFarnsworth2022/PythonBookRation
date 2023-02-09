def BookReadingRatio(TotalPages, PagesRead, MinutesToReadPages):
    RemainingPages = TotalPages - PagesRead
    PagePerMinuteReadingRatio = MinutesToReadPages / PagesRead
    TimeToReadRemainingPages = RemainingPages * PagePerMinuteReadingRatio
    HoursToReadPages = MinutesToReadPages/60
    print("You are reading a book with " + str(TotalPages) + " pages.")
    print("You read " + str(PagesRead) + " pages in " + str(HoursToReadPages)+ " hours or " + str(MinutesToReadPages) +  " minutes.")
    print("Your minutes per page ratio is " + str(PagePerMinuteReadingRatio) + " minutes per page.")
    print("You have " + str(TotalPages) + " - " +  str(PagesRead) + " = " + str(RemainingPages) + " remaining to read.")
    print("With " + str(RemainingPages) + " remaining pages to read * the page per minute ratio of " + str(PagePerMinuteReadingRatio) + " = " + str(TimeToReadRemainingPages) + " minutes."  )
    return TimeToReadRemainingPages

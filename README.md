# HW4: Exceptions and unit tests
In HW1, you downloaded the data from https://data.seattle.gov/resource/4xy5-26gy.csv and put it in a data directory.
In general, we don't keep data in github because of limitations on github storage.

In this homework, you will develop a function and related tests to manage downloaded data. You will use
a technique that is very common in software engineering called *data caching*. You will implement two functions. Both
have a single argument, a URL of a data you want to access. The first function, get_data, downloads the data if it
is not present locally; if the data are already present, then it takes no action. The second function, delete_data, removes
the data if it is present locally.

The grading rubric is:

- Correctly implement get_data with an exception if the URL does not exist. (Hint: Try downloading the file using urllib3 instead of wget.) (2 pt)
- Correctly implement remove_data (1/2 pt)
- Implement tests for get_data that consider the following cases: (a) file is present locally; (b) file is not present locally, and the URL points to a file that exists; and (c) URL does not point to a file that exists. (2 pt)
- Correctly implement tests for remove_data (1/2 pt)

Tests should be in a separate file from the functions get_data and remove_data.

8/8

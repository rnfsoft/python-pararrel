https://monkey3199.github.io/develop/python/2018/12/04/python-pararrel.html


    # START, END  = 0, 100
    # Result with One Thread: 4950 0.0009984970092773438
    # Result with Two Threads: 4950 0.0
    # Result with Two Multiprocessings: 4950 0.24685907363891602

    # START, END  = 0, 10000000
    # Result with One Thread: 49999995000000 2.4322712421417236
    # Result with Two Threads: 49999995000000 1.879253625869751
    # Result with Two Multiprocessings: 49999995000000 1.376906156539917

    # START, END  = 0, 100000000
    # Result with One Thread: 4999999950000000 19.144771099090576
    # Result with Two Threads: 4999999950000000 19.0737144947052
    # Result with Two Multiprocessings: 4999999950000000 12.827365159988403
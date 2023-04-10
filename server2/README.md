<p>
This is an api that works as a middleman between our elastic servers and applications,
it's built for speed and should be prefered over the older method of using the es-connector
library.
</p>

<p>
Any bugs should be reported on the hive git found at this address https://git.corp.adobe.com/TechOps-NetEng/hive
In the issues tab.
</p>

<p>
Implemented apis documentation can be found here
https://api-dev.ne.adobe.net/elasticsearch/docs
</p>
<p>
For testing you can go into the apps/test/service_tests directory and run pytest test_elasticsearch.py
For faster run it is recommended to install pytest-xdist and run with pytest -n auto
</p>
*******************************************************
Alternative Recommender Case Study
*******************************************************

:Authors: Adam Richards
:Web site: https://github.com/zipfian/alt-recommender-case-study
:Copyright: Galvanize

About
-----------------------------------------------

The original case study
https://github.com/zipfian/recommender-case-study relied heavily on
GraphLab.  This repository is an alternative that guides
students towards one of two alternative technologies.

Team organization
---------------------

Students can choose one of two possible routes to a solution.  The day
before the case study students are asked if they would like to pursue
a solution that will **improve their big data skills** or alternatively a
solution that will **improve their machine learning skills**.  Both sound
tempting, but team dynamics are likely improved if all members are
concentrated on the same technology when it comes to a solution.

  It can be helpful to provide the links below the day before the case study
  so that students have time to familiarize themselves with the underlying concepts.

Spark and a the big data solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Spark solution makes use of the Machine Learning library ML.  The
following two links will help you build a solution.  It is assumed
that the students who decide to build a recommender in Spark have
already completed the Spark lectures and assignments.

  * https://spark.apache.org/docs/latest/ml-collaborative-filtering.html
  * https://www.codementor.io/jadianes/building-a-recommender-with-apache-spark-python-example-app-part1-du1083qbw

The first link is the official documentation.  The second is a
solution posted in a blog and although it uses MLlib instead of ML it
is still a useful resource.  ML should be used is the more stable library.
    
PyMC3 and the probabilistic solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The probabilistic solution makes use of PyMC3.  The following links
are provided as resources to help you build a solution.  It is assumed
that the students who decide to build a recommender in PyMC3 have had
at least some exposure to PyMC3 in one or more lectures.

  * https://pymc-devs.github.io/pymc3/notebooks/pmf-pymc.html
  * https://github.com/zipfian/probabilistic-programming-intro  

The first link is where students will spend most of their time.  The
second link is a talk that introduces PyMC3 and some of the resources
contained therein are useful for providing context.

The Case Study
--------------------------------------

You a the team of talented data scientists working for the company,
**Items-Legit**, who uses several production recommenders that provide
a significant revenue stream.  The issue is that they have been
around a long time and your head of data science has asked you to
explore new solutions.

The solution that has been around for so long is called the **Mean of
Means**.  We see that some users like to rate things highly---others
simply do not.  Some items are just better or worse.  We can capture
these general trends through per-user and per-joke rating means. We
also incorporate the global mean to smooth things out a bit. So if we
see a missing value in cell R_{ij}, we'll average the global
mean with the mean of U_i and the mean of V_j and use
that value to fill it in.

We would like you to use this as a baseline when making your
comparisons.  An implementation of this baseline and several others
are described in the `PyMC3 example
<https://pymc-devs.github.io/pymc3/notebooks/pmf-pymc.html>`_.  They
are provided for you in `Baselines.py`.
   
At the end of the day you are to present your solution to the bosses
and the entire product team.  You can assume that they have a
reasonable depth of knowledge in statistics and big data technologies.

The main goal here is to improve the RMSE, however, another equally
important goal is to present your model and the details of your method
in a clear, but technically sound manner.  *You need to convince us
that you understand the tools you are using AND that it is a better
way forward.*  We would also like you to include some discussion about
how you would move from prototype to production.

The data
--------------

Since we are a company with several unrelated product lines that
require different recommendation engines there are two data sets we
would like you to try out your engine on: the **jokes data set** and
the **movies data set**.

The spark example makes use of the movies dataset.

   * https://www.codementor.io/jadianes/building-a-recommender-with-apache-spark-python-example-app-part1-du1083qbw

And the PyMC3 example makes use of the jokes dataset.

   * https://pymc-devs.github.io/pymc3/notebooks/pmf-pymc.html

So natuarlly we are asking you do to do both.

There are larger versions of these data sets available from the links
below, but we do not expect a production ready recommender in only a
days time so do not worry too much about scale for now.  If you are
interested we provide the links as a reference.

  * https://grouplens.org/datasets/movielens
  * http://eigentaste.berkeley.edu/dataset/  

You may improve upon, scale (up or down) and deploy your system in the manner
that your team feels is best.  Good luck!

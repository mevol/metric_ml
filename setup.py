from setuptools import setup

setup(
    name = "metrix_ml",
    version = "0.0.1",
    author = "Melanie Vollmar",
    author_email = "melanie.vollmar@diamond.ac.uk",
    description = "A package which uses crystallographic statistics and metrics \n"
    							"to make predictions about the likelihood of solving a structure",
    license = "BSD",
    keywords = "awesome python package",
    packages=[
      'metrix_ml'
    ],
    scripts=[
      'bin/decisiontree_gridsearch',
      'bin/decisiontree_gridsearch_database',
      'bin/decisiontree_gridsearch_database_features',
      'bin/decisiontree_gridsearch_man_add',
      'bin/decisiontree_gridsearch_man_add_features',
      'bin/decisiontree_randomsearch',
      'bin/decisiontree_bag_gridsearch',
      'bin/decisiontree_bag_randomsearch',
      'bin/randomforest_gridsearch',   
      'bin/randomforest_randomsearch',
      'bin/randomforest_ada_gridsearch',
      'bin/randomforest_ada_randomsearch',
      'bin/feature_correlations',
      'bin/decisiontree_gridsearch_prot_screen_trans',
      'bin/decisiontree_gridsearch_prot_screen_trans_features',
      'bin/decisiontree_gridsearch_transform',
      'bin/decisiontree_gridsearch_transform_features',
      'bin/decisiontree_randomsearch_prot_screen_trans',
      'bin/decisiontree_randomsearch_transform',
      'bin/decisiontree_randomsearch_man_add',
      'bin/decisiontree_randomsearch_man_add_features',
      'bin/decisiontree_randomsearch_database_features',
      'bin/decisiontree_randomsearch_database',
    ],
    install_requires=[
      'matplotlib',
      'pandas',
      'pytest',
      'sklearn',
      'scikit-plot',
      'scipy'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)

import os
import modal
    
LOCAL=True

stub = modal.Stub()

hopsworks_image = modal.Image.debian_slim().pip_install(["hopsworks"])


@stub.function(image=hopsworks_image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("jim-hopsworks-ai"))
def f():
    g()

def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()
    iris_df = pd.read_csv("https://repo.hops.works/master/hopsworks-tutorials/data/iris.csv")
    iris_fg = fs.get_or_create_feature_group(
        name="iris_modal",
        version=1,
        primary_key=["sepal_length","sepal_width","petal_length","petal_width"], 
        description="Iris flower dataset")
    iris_fg.insert(iris_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        with stub.run():
            f()
# Local run

1. Open terminal.
1. Go into `bloomon-code-challenge` folder.
1. You will need to install python 3.7.0.
1. Run:
    ```
    python script.py
    ```
1. In current (`bloomon-code-challenge`) folder you will see new file `output.txt`. It will contain results for this test task.

You can specify input file name and output file name by passing following flags:
* `--input-file-name` for input file name (default is `sample.txt`);
* `--output-file-name` for output file name (default is `output.txt`);

So, you can run following command:
```
python script.py --input-file-name another_sample.txt --output-file-name another_output.txt
```

# Run in Docker

I tested this program on MacOS and I'm not sure how it will work on Windows, for example.

1. Open terminal.
1. Go into `bloomon-code-challenge` folder.
1. Run:
    ```
    docker build . --tag bloomon:oleh
    ```
    It will create docker image.
1. Run:
    ```
    docker run -it --name bloomon-code-olehzorenko --mount src="$(pwd)",target=/app,type=bind bloomon:oleh
    ```
    It will run container, mount volumes and execute program for this test task.
1. In current (`bloomon-code-challenge`) folder you will see new file `output.txt`. It will contain results for this test task.

In Docker you also can specify input file name and output file name by passing following flags:
* `--input-file-name` for input file name (default is `sample.txt`);
* `--output-file-name` for output file name (default is `output.txt`);

So, you can run following command:
```
docker run -it --name bloomon-code-olehzorenko --mount src="$(pwd)",target=/app,type=bind bloomon:oleh --input-file-name another_sample.txt --output-file-name another_output.txt
```
In this case, please, remember that you already have container with `bloomon-code-olehzorenko` name and if you need to run it again with file names flags, change the name of the container by setting `--name` flag to another name, for example `--name bloomon-code-olehzorenko-with-flags`.

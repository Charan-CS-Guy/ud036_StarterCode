# TMDB Top Movies

"TMDB Top Movies" is a Movie Trailer website, which fetches the top popular movies from [TMDB](https://www.themoviedb.org/en) and displays their posters and titles along with the trailers.

## Install

* Install python on your system (desktop or laptop).

* Install [pip](https://pip.pypa.io/en/stable/installing/)
  * pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4 binaries downloaded from python.org, but you'll need to [upgrade pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip).

    * Else, To install pip,  download [get-pip.py](https://bootstrap.pypa.io/get-pip.py).

    * Then run the following command:

    ```python
    python get-pip.py
    ```
* Install the following modules:

    * requests

    ```python
    pip install requests
    ```

    * simplejson

    ```python
    pip install simplejson
    ```

    * configobj

    ```python
    pip install configobj
    ```

* Download/clone the above repository.

* After successfully installing python and downloading/cloning the repo, change the config file in the repo:

    * open config.ini file and provide your [api_key of TMDB](https://developers.themoviedb.org/3/getting-started)

* and execute the following commands in the present directory:

```python
    python entertainment_center.py
```

* Or, just run the **entertainment_center.py** python file using any text editor / IDE that supports python. (such as :- [Sublime Text](https://www.sublimetext.com/), [Visual Studio Code](https://code.visualstudio.com/), etc..)

## Contribution

You can contribute to the repo by modifying the web site interface and using API's to create objects for movies, etc..

## License

The content of this repository is licensed under ae [LICENSE](LICENSE.md) file.

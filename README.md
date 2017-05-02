# Behave-Cachet

Behave-Cachet is an experimental project ...

The original's project's are:

[Cachet](https://github.com/cachethq/Cachet) is a beautiful and powerful open source status page system, a free replacement for services such as StatusPage.io, Status.io and others.

[Behave](https://github.com/behave/Behave) is ...


# SETUP

To run the project ...

# First Steps

1.  Clone the Behave-Cachet repo

  ```shell
  git clone https://github.com/yurireeis/BehaveCachet.git
  cd BehaveCachet
  ```

2. Make a virtualenv with Python 3.x and activate it:

  ```shell
  virtualenv ~/${your_virtualenv_path}/behave-cachet -p python3
  source ~/${your_virtualenv_path}/behave-cachet/bin/activate
  ```

3. Install the project dependencies (cachet-wrapper is included here!):

  ```shell
  pip install -r requirements.txt
  ```

# Set up Behave

1. Download browser drivers binaries in some exec path (Linux):

- [PhantomJS Driver](http://phantomjs.org/download.html)
- [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

ps.: Firefox Driver comes as default.

2. Give exec permissions to browser drivers:

example:

```shell
sudo chmod +x {driver path}/{drivers file}
```

3. Execute:

ps.: in the project path

```shell
behave
```

# Running Cachet/Jenkins with docker


1. Clone the Cachet Docker project

  ```shell
  git clone https://github.com/cachethq/Docker.git cachet-docker
  ```

2. Build and up BehaveCachet project

  ```shell
  docker-compose build
  docker-compose up
  ```

3. Initialize the database and set a key:

  ```shell
  docker ps  # to grab cachet instance name or id
  docker exec -i ${your_cachet_instance_name_or_id}  php artisan key:generate
$ docker exec -i ${your_cachet_instance_name_or_id}  php artisan app:install
  ```

4. Open a browser and access Cachet to setup:

  ```browser
  http://<ipcachetisboundto>/setup
  ```

5. Open the browser and configure Jenkins:
  ```browser
  http://<ipjenkinsisboundto>:8080
  ```

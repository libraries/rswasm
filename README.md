# Rswasm

This project shows how to compile a rust library to a wasm library using only `cargo`.

## Compile

The example project is a function that calculates pi.

```sh
$ rustup target add wasm32-unknown-unknown
$ cargo build
```

## Run

```sh
$ pip install pywasm
$ python script/run.py
# pi = 3.1415926535901733
```

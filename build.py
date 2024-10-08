#!/usr/bin/env python3

import os
import subprocess

import click


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--hexrays_sdk",
    "hexrays_sdk",
    type=str,
    default=str(),
    help="path to hexrays_sdk directory",
)
@click.argument("idasdk")
def build_plugin(idasdk: str, hexrays_sdk: str):
    """Build efiXplorer plugin"""

    os.chdir("efiXplorer")

    if not os.path.isdir("build"):
        os.mkdir("build")

    os.chdir("build")

    command = ["cmake", "..", f"-DIdaSdk_ROOT_DIR={idasdk}"]
    if hexrays_sdk:
        print("[INFO] HexRays analysis will be enabled")
        command.append(f"-DHexRaysSdk_ROOT_DIR={hexrays_sdk}")
    subprocess.call(command)
    subprocess.call(["cmake", "--build", ".", "--config", "Release", "--parallel"])


@click.command()
@click.argument("idasdk")
def build_loader(idasdk: str):
    """Build efiXloader"""

    os.chdir("efiXloader")

    if not os.path.isdir("build"):
        os.mkdir("build")

    os.chdir("build")

    command = ["cmake", "..", f"-DIdaSdk_ROOT_DIR={idasdk}"]
    subprocess.call(command)
    subprocess.call(["cmake", "--build", ".", "--config", "Release", "--parallel"])


@click.command()
@click.option(
    "--hexrays_sdk",
    "hexrays_sdk",
    type=str,
    default=str(),
    help="path to hexrays_sdk directory",
)
@click.argument("idasdk")
def build_everything(idasdk: str, hexrays_sdk: str):
    """Build plugin (efiXplorer) and loader (efiXloader)"""

    if not os.path.isdir("build"):
        os.mkdir("build")

    os.chdir("build")

    command = ["cmake", "..", f"-DIdaSdk_ROOT_DIR={idasdk}"]
    if hexrays_sdk:
        print("[INFO] HexRays analysis will be enabled")
        command.append(f"-DHexRaysSdk_ROOT_DIR={hexrays_sdk}")
    subprocess.call(command)
    subprocess.call(["cmake", "--build", ".", "--config", "Release", "--parallel"])


cli.add_command(build_plugin)
cli.add_command(build_loader)
cli.add_command(build_everything)


if __name__ == "__main__":
    cli()

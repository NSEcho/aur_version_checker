# aur_version_checker

This script is created in order to maintain aur package versions because I don't like seeing those _Flagged out-of-date_ red messages.

Script expects two arguments:
* maintainer name
* file containing list of packages

File that the script reads consists of three fields separated with space:
1. package name (the same as AUR package name)
2. url where to check for new relases
3. regex to search version

Example of file:
```
$ cat packages.txt
rclone-browser https://github.com/kapitainsky/RcloneBrowser/releases (?<=Rclone\sBrowser\s)[^<]+
blink https://github.com/AGProjects/blink-qt/releases (?<=release-)\d[^<"]+
bim https://github.com/klange/bim/releases (?<=releases/tag/v)[^"]+
```

__Note:__ In your regex, replace space with ```\s```

# Running 

```
$ ./checker.py init packages.txt
[-] Package rclone-browser is outdated
[*] Package blink is up to date
[*] Package bim is up to date
```

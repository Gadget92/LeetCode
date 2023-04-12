def simplifyPath(path: str) -> str:
    location = []
    for step in path.split("/"):
        if step in (".", ""):
            pass
        elif step == "..":
            if location: 
                location.pop()
        else:
            location.append(step)

    return "/" + "/".join(location)



if __name__ == "__main__":
    print(simplifyPath("/home/")) 
    print(simplifyPath("/../")) 
    print(simplifyPath("/home//foo/")) 
    print(simplifyPath("/a/./b/../../c/"))
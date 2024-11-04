def is_pangram(st) -> bool:
    st = st.lower()
    return set("abcdefghijklmnopqrstuvwxyz") <= set(st)

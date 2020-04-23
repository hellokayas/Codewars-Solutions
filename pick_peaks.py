def pick_peaks(arr):
    n = len(arr)
    if arr == []:
        return {"pos":[],"peaks":[]}
    Diff = []
    for i in range(0,n-1):
        if arr[i]< arr[i+1]:
            Diff.append(1)
        elif arr[i] == arr[i+1]:
            Diff.append(0)
        if arr[i] > arr[i+1]:
            Diff.append(-1)
    pos = []
    peaks = []
    j = 0
    for i in range(0,n-2):
        if Diff[i] == 1 and Diff[i+1] == -1:
            pos.append(i+1)
            peaks.append(arr[i+1])
        if Diff[i] == 1 and Diff[i+1] == 0:
            if Diff[i+1:] == [Diff[i+1]]:
                break
            j = i+1
            while(Diff[j] == 0 and j < n-2):
                j = j+1
            if Diff[j] == -1:
                pos.append(i+1)
                peaks.append(arr[i+1])
        
            
    return {"pos":pos, "peaks":peaks}

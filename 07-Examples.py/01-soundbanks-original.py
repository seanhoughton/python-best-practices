import os, stat

APPROVED_EXTS = ['.dcs']


def go():
    soundBankArray = [[]]

    for root, dirs, files in os.walk( '.' ):
        for name in files:
            base, ext = os.path.splitext(name)
            if ext.lower() not in APPROVED_EXTS:
                continue
            dcsPath = os.path.abspath(os.path.join(root, name))
            dcsFile = open(dcsPath, 'r')
            for line in dcsFile:
                if "tActionSound" in line:
                    lineParts = line.split('"')
                    for linePart in lineParts:
                        if 'SND_' in linePart:
                            linePart = linePart.replace('SND_','')
                            newSoundBank = 1
                            count = 0
                            for soundBank in soundBankArray:
                                if len(soundBank):
                                    if soundBank[0] == linePart:##check to see if the soundBank is already in the array.
                                        newSoundBank = 0
                                        break
                                count = count+1
                            if newSoundBank:
                                soundBankArray.append([linePart])
                                soundBankArray[count].append(dcsPath)
                            else:
                                newPath = 1
                                for existingPath in soundBankArray[count]:
                                    if existingPath == dcsPath:
                                        newPath = 0
                                        break
                                if newPath:
                                    dcsPathC = dcsPath.rstrip()
                                    soundBankArray[count].append(dcsPath)

    for info in soundBankArray:
        print '\n\n'
        count = 0
        for line in info:
            if count > 0:
                print '\t'
            print line,
            count = count + 1
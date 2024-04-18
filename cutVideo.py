import subprocess
import os
# subprocess.call(['ffmpeg', '-i', r'D:\SM-APPS-KOLIBRI\video.mp4','-ss', '00:00:20', '-to', '00:01:45', '-c:v', 'copy','-c:a','copy', 'outputfile.mp4'])
# subprocess.call(['ffmpeg', '-i', r'D:\SM-APPS-KOLIBRI\video.mp4','-ss', '00:02:15', '-to', '00:04:00', '-c:v', 'copy','-c:a','copy', 'outputfile2.mp4'])
# subprocess.call(['ffmpeg','-i','concat:outputfile.mp4|outputfile2.mp4','-c','copy','final.mp4'])

def cutMultipleVideo(input_video_path: str, name: str, ext: str, cortes: list[list[str]], outdir: str):
    file_dir = os.path.join(outdir, name)
    file_txt = os.path.join(file_dir, 'files.txt')

    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    if os.path.exists(file_txt):
        os.remove(file_txt)

    filetxt = open(file_txt, mode='a+', encoding='utf-8')
    filetxt.write('# primer línea\n')

    for index, corte in enumerate(cortes):
        inicio = corte[0]
        fin = corte[1]
        filename = f'{name}part{index}.{ext}'
        filedir = os.path.join(file_dir, filename)

        subprocess.run(['ffmpeg', '-i', input_video_path, '-ss', inicio, '-to', fin, filedir], check=True)

        filetxt.write(f"file '{filedir}'\n")

    filetxt.close()

    out_filename = os.path.join(outdir, f'{name}.mp4')

    subprocess.run(['ffmpeg','-fflags','+genpts','-f', 'concat', '-safe', '0', '-i', f'{file_txt}', '-c', 'copy', f'{out_filename}'], check=True)
    
# cutMultipleVideo(r'D:\SM-APPS-KOLIBRI\video.mp4','1234','mp4',[['00:00:00', '00:01:00'], ['00:01:08', '00:07:26'], ['00:08:25', '00:09:26']],r'D:\SM-APPS-KOLIBRI\video-editor\videos')

def cutSingleVideo(input_video_path: str, name: str, ext: str, cortes: list[str], outdir: str):
    file_dir = os.path.join(outdir)
    # if not os.path.exists(file_dir):
    #     os.mkdir(file_dir)
    
    inicio = cortes[0]
    fin = cortes[1]
    filename = f'{name}.{ext}'
    filedir = os.path.join(file_dir, filename)

    subprocess.run(['ffmpeg', '-i', input_video_path, '-ss', inicio, '-to', fin, filedir], check=True)

#cutSingleVideo(r'D:\SM-APPS-KOLIBRI\video.mp4','1234','mp4',['00:00:00', '00:01:00'],r'D:\SM-APPS-KOLIBRI\video-editor\videos')
    
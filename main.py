import os
import cutVideo
import readCSV

CSV_PATH = os.path.join(os.getcwd(),'pruebas-multi.csv')
INPUT_FOLDER = r'D:\SM-APPS-KOLIBRI\PARA-PASAR-A-NUC\16-04-24-VIDEOS-RESUBIR\original'
OUTPUT_FOLDER = r'D:\SM-APPS-KOLIBRI\PARA-PASAR-A-NUC\16-04-24-VIDEOS-RESUBIR\edits'

def main():
    items = readCSV.readDataCSV(CSV_PATH)
    path_log_not_found = os.path.join(os.getcwd(),'logs','ids_not_found_pruebas.txt') 
    path_log_erros = os.path.join(os.getcwd(),'logs','erros_pruebas.txt') 
    
    if os.path.exists(path_log_not_found):
        os.remove(path_log_not_found)
    log_not_found = open(path_log_not_found,mode='+a',encoding='utf-8')
    
    if os.path.exists(path_log_erros):
        os.remove(path_log_erros)
    log_erros = open(path_log_erros,mode='+a',encoding='utf-8')
    
    print(f'[***** {len(items)} PARA EDITAR *****]')
    
    count = 0
    
    for item in items:
        id = item['id']
        cortes = item['cortes']
        
        exist = os.path.join(OUTPUT_FOLDER,f'{id}.mp4')
        
        if os.path.exists(exist):
            count += 1
            print(f'ID {id} YA FUE EDITADO')
            continue
        
        radis_list = os.listdir(INPUT_FOLDER) 
        radi_founded = False
        input_video_path = ''
        for radi in radis_list:
            if f'{id}.' in radi and '.mp4' in radi:
                radi_founded = True
                input_video_path = os.path.join(INPUT_FOLDER,radi)
                break
        if not radi_founded:
            log_not_found.write(f'{id},\n')
            continue
        try:
            if type(cortes[0]) == str:
                print('CORTE SIMPLE')
                cutVideo.cutSingleVideo(input_video_path,f'{id}','mp4',cortes,OUTPUT_FOLDER)
                count += 1
            elif type(cortes[0]) == list:
                print('CORTE MULTIPLE')
                cutVideo.cutMultipleVideo(input_video_path,f'{id}','mp4',cortes,OUTPUT_FOLDER)
                count += 1
        except Exception as e:
            print(f'[!!!!! ERROR AL EDITAR {id} !!!!!]')
            log_erros.write(f'ID {id} ERROR {e}\n')
            continue
    
    print(f'[***** SE EDITARON {count} DE {len(items)} VIDEOS *****]')
main()
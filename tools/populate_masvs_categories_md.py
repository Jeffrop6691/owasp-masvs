import os
import yaml
import argparse

def write_controls_content(control, cf):          
    h1 = '##'
    h2 = '###'
    final_newline = '\n'
    
    cf.write(f'{h1} {control["id"]}\n\n')
    cf.write(f'{h2} Statement\n\n')
    cf.write(f'{control["statement"]}\n\n')
    cf.write(f'{h2} Description\n\n')
    cf.write(f'{control["description"]}\n{final_newline}')


def yaml_to_md(input_file, for_website):

    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    for group in data['groups']:
        group_id = group['id']
        controls = group['controls']

        for file in sorted(os.listdir("Document")):
            if "-MASVS-" in file:
                # group_id_in_file is the part of the filename after the first dash and without the extension
                group_id_in_file = file.split("-")[1] + "-" + file.split("-")[2].split(".")[0]
               
                if group_id_in_file == group_id:
                    with open(os.path.join("Document", file), "a") as f:
                        f.write('\n')
                        f.write('| ID | Statement |\n')
                        f.write('|----|-----------|\n')
                        for control in controls:
                            if for_website == True:
                                control_id = f'[{control["id"]}](controls/{control["id"]})'
                            else:
                                control_id = control["id"]
                            
                            f.write(f'| {control_id} | {control["statement"]} |\n')
                        
                        f.write('\n')
                        f.write('<!-- \pagebreak -->\n\n')
                    
                        if for_website == False:
                            for control in controls:
                                write_controls_content(control, f)
                print(f'Successfully wrote to {file}')

# get input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input file", required=False, default="masvs.yaml")
parser.add_argument("-w", "--website", help="Generate for website", action='store_true', required=False, default=False)
args = parser.parse_args()

input_file = args.input
for_website = args.website

yaml_to_md(input_file, for_website)

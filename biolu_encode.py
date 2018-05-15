import argparse

parser = argparse.ArgumentParser(description='Change encoding from BIO to BIOLU')
parser.add_argument('input', metavar='-i', type=str, help='The path to the original file with BIO encoding')
parser.add_argument('output', metavar='-o', type=str, help='The name of your BIOLU encoded file')
args = parser.parse_args()

input_file = args.input
output_file = args.output


def read_file(input_file):
    with open(input_file, 'rb') as f:
        return f.read().decode('ASCII').split('\n')


def write_line(new_label: str, prev_label: str, line_content: list, output_file):
    new_iob = new_label + prev_label
    line_content[3] = new_iob
    current_line = ' '.join(line_content)
    output_file.write(current_line + '\n')


def convert(input_file, output_path):
    output_file = open(output_path, 'w')

    for i in range(len(input_file) + 1):

        try:
            current_line = input_file[i]

            if '-DOCSTART-' in current_line:
                output_file.write(current_line + '\n')
            elif len(current_line) == 0:
                output_file.write(current_line + '\n')

            else:
                prev_iob = None
                next_iob = None
                prev_line = None
                next_line = None

                try:
                    prev_line = input_file[i - 1]
                    next_line = input_file[i + 1]

                    if len(prev_line) > 0:
                        prev_line_content = prev_line.split()
                        prev_iob = prev_line_content[3]

                    if len(next_line) > 0:
                        next_line_content = next_line.split()
                        next_iob = next_line_content[3]

                except IndexError:
                    pass

                current_line_content = current_line.split()
                current_iob = current_line_content[3]

                # Outside entities
                if current_iob == 'O':
                    output_file.write(current_line + '\n')

                # Unit length entities
                elif (prev_iob == 'O' or len(prev_line) == 0) and next_iob == 'O':
                    write_line('U-', current_iob[2:], current_line_content, output_file)

                # First element of chunk
                elif (prev_iob == 'O' or len(prev_line) == 0) and next_iob != 'O':
                    write_line('B-', current_iob[2:], current_line_content, output_file)

                # Last element of chunk
                elif (prev_iob != 'O' and len(prev_line) != 0) and (next_iob == 'O' or len(next_line) == 0):
                    write_line('L-', current_iob[2:], current_line_content, output_file)

                # Inside a chunk
                elif (prev_iob != 'O' and len(prev_line) != 0) and (next_iob != 'O' and len(next_line) != 0):
                    write_line('I-', current_iob[2:], current_line_content, output_file)

        except IndexError:
            pass

bio = read_file(input_file)
convert(bio, output_file)

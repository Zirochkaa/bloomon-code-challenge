import argparse

from logic import get_bouquets


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file-name', '-if', help='Name of file with bouquets data.',
                        type=str, default='sample.txt')
    parser.add_argument('--output-file-name', '-of', help='Name of file to which write bouquets data.',
                        type=str, default='output.txt')
    args = parser.parse_args()

    get_bouquets(input_file_name=args.input_file_name, output_file_name=args.output_file_name)

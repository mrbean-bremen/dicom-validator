import argparse
import json
import os

from pydicom import filereader

from dcm_spec_tools.spec_reader.part3_reader import Part3Reader
from dcm_spec_tools.spec_reader.part4_reader import Part4Reader
from dcm_spec_tools.spec_reader.part6_reader import Part6Reader
from dcm_spec_tools.validator.iod_validator import IODValidator


def main():
    parser = argparse.ArgumentParser(
        description='Validates DICOM file IODs')
    parser.add_argument('dicomfile', help='Path of DICOM file to validate')
    parser.add_argument('--standard-path', '-src',
                        help='Path with the DICOM specs in docbook format',
                        default='./DICOM')
    parser.add_argument('--json-path', '-json',
                        help='Path with the DICOM specs in JSON format')
    args = parser.parse_args()
    if args.json_path:
        with open(os.path.join(args.json_path, 'iod_info.json')) as info_file:
            iod_info = json.load(info_file)
        with open(os.path.join(args.json_path, 'module_info.json')) as info_file:
            module_info = json.load(info_file)
    else:
        dict_info = Part6Reader(args.standard_path).data_elements()
        part3reader = Part3Reader(args.standard_path, dict_info)
        iod_per_chapter_info = part3reader.iod_descriptions()
        chapter_info = Part4Reader(args.standard_path).iod_chapters()
        iod_info = {chapter_info[chapter]: iod_per_chapter_info[chapter]
                    for chapter in iod_per_chapter_info if chapter in chapter_info}
        module_info = part3reader.module_descriptions()

    data_set = filereader.read_file(args.dicomfile, stop_before_pixels=True, force=True)
    return len(IODValidator(data_set, iod_info, module_info).validate())


if __name__ == '__main__':
    exit(main())

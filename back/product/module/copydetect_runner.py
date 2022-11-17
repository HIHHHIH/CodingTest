from copydetect import CopyDetector

def run_detector():
    detector = CopyDetector(test_dirs=["tests"],extensions=["py"],display_t=0.5)
    detector.add_file("./test.py")
    detector.run()

    detector.get_copied_code_list()
    return


run_detector()
# LFIprobe 

LFIprobe is a command-line tool designed to test for Local File Inclusion (LFI) vulnerabilities in web applications. It allows you to specify a target URL including the vulnerable URI path and parameter, and then attempts to include files from the server to detect potential LFI vulnerabilities. 

## Installation 

1. Clone the repository:

```
git clone https://github.com/4xura/LFIprobe
```

2. Navigate to the directory: 

```
cd LFIprobe
```

3. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

```
python3 LFIprobe.py -u <target_url_include_vulnerable_path>
```

Replace `<target_url_include_vulnerable_path>` with the URL of the vulnerable web application including the vulnerable URI path and parameter. 

**Sample Usage:**

```
python3 LFIprobe.py -u http://example.com/download.php?file=
```

## License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer 

This tool is intended for educational and testing purposes only. Use it responsibly and only on systems that you have explicit permission to test.
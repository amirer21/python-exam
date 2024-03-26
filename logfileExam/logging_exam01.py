import logging

# Configure logging
logging.basicConfig(
    filename='example.log',  # Log file
    level=logging.DEBUG,  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def example_function():
    try:
        # Your code here
        result = 10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Log the error along with the traceback
        logging.error("An error occurred: %s", str(e), exc_info=True)

def main():
    # Log a debug message
    logging.debug("This is a debug message")

    # Log an info message
    logging.info("This is an info message")

    # Log a warning message
    logging.warning("This is a warning message")

    # Call the function that might raise an exception
    example_function()

if __name__ == "__main__":
    main()

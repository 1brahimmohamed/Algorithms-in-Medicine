#include <iostream>
#include <queue>
#include <vector>

struct Request {
    Request(int arrival_time, int process_time) :
            arrival_time(arrival_time),
            process_time(process_time) {}

    int arrival_time;
    int process_time;
};

struct Response {
    Response(bool dropped, int start_time) :
            dropped(dropped),
            start_time(start_time) {}

    bool dropped;
    int start_time;
};

class Buffer {
public:
    Buffer(int size) :
            size_(size),
            finish_time_() {}

    Response Process(const Request &request) {

        /** if the time of the time of the arriving request is more than the maximum time
         * then the max time is the new arrival time
        **/
        if (request.arrival_time > maxTime)
            maxTime = request.arrival_time;

        /**
         * as long as the queue of the finish time is not empty & current request arrival time is more than the queue
         * finish time, then pop the finish time from the queue
        **/
        while (!finish_time_.empty() && request.arrival_time >= finish_time_.front()) {
            finish_time_.pop();
        }

        // number of packets in buffer
        size_t packetsCount = finish_time_.size();

        /** if the number of packets in the buffer is less than the buffer size
         *  then get the current queue finish time and store it and increase the max time with the current request process
         *  time then push the max time into the finish_time queue
         *  return false (not dropped), the start time of the request (buffer finish time before the requests comes)
         **/
        if (packetsCount < size_) {
            int bufferFinishTime = maxTime;
            maxTime += request.process_time;
            finish_time_.push(maxTime);

            return Response(false, bufferFinishTime);
        }

        /**  if the buffer is full then return true & -1   **/
        else {
            return Response(true, -1);
        }
    }

private:
    int size_;
    int maxTime = 0;
    std::queue<int> finish_time_;
};

std::vector<Request> ReadRequests() {
    std::vector<Request> requests;
    int count;
    std::cin >> count;
    for (int i = 0; i < count; ++i) {
        int arrival_time, process_time;
        std::cin >> arrival_time >> process_time;
        requests.push_back(Request(arrival_time, process_time));
    }
    return requests;
}

std::vector<Response> ProcessRequests(const std::vector<Request> &requests, Buffer *buffer) {
    std::vector<Response> responses;
    for (int i = 0; i < requests.size(); ++i)
        responses.push_back(buffer->Process(requests[i]));
    return responses;
}

void PrintResponses(const std::vector<Response> &responses) {
    for (int i = 0; i < responses.size(); ++i)
        std::cout << (responses[i].dropped ? -1 : responses[i].start_time) << std::endl;
}

int main() {
    int size;
    std::cin >> size;
    std::vector<Request> requests = ReadRequests();

    Buffer buffer(size);
    std::vector<Response> responses = ProcessRequests(requests, &buffer);

    PrintResponses(responses);
    return 0;
}

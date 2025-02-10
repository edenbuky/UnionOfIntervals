#################################
# Your name:
#################################

import numpy as np
import matplotlib.pyplot as plt
import intervals


class Assignment2(object):
    """Assignment 2 skeleton.

    Please use these function signatures for this assignment and submit this file, together with the intervals.py.
    """

    def sample_from_D(self, m):
        """Sample m data samples from D.
        Input: m - an integer, the size of the data sample.

        Returns: np.ndarray of shape (m,2) :
                A two dimensional array of size m that contains the pairs where drawn from the distribution P.
        """
        x_values = np.random.uniform(0, 1, m)
        y_values = np.zeros(m)
        for i, x in enumerate(x_values):
            if x <= 0.2 or (0.4 <= x <= 0.6) or x >= 0.8:
                p_y_given_x = 0.8
            else:
                p_y_given_x = 0.1

            y_values[i] = np.random.choice([0, 1], p=[1 - p_y_given_x, p_y_given_x])

        samples = np.column_stack((x_values, y_values))

        sorted_indices = np.argsort(samples[:, 0])
        sorted_samples = samples[sorted_indices]

        return sorted_samples

    def calculate_true_error(self, hypothesis_intervals):
        error = 0
        # Define the regions where P(Y=1|X=x) = 0.8 and P(Y=1|X=x) = 0.1
        high_prob_regions = [(0, 0.2), (0.4, 0.6), (0.8, 1)]
        low_prob_regions = [(0.2, 0.4), (0.6, 0.8)]

        # Calculate error in regions where hypothesis predicts Y=1
        for interval in hypothesis_intervals:
            # Integrate P(Y=0|X=x) over each interval where h predicts Y=1
            for region in high_prob_regions:
                if interval[0] < region[1] and interval[1] > region[0]:  # If the interval overlaps with high probability region
                    # Integrate 0.2 (P(Y=0|X=x)) over the overlap
                    overlap = min(interval[1], region[1]) - max(interval[0], region[0])
                    error += overlap * 0.2
            for region in low_prob_regions:
                if interval[0] < region[1] and interval[1] > region[0]:  # If the interval overlaps with low probability region
                    # Integrate 0.9 (P(Y=0|X=x)) over the overlap
                    overlap = min(interval[1], region[1]) - max(interval[0], region[0])
                    error += overlap * 0.9

        # Calculate error in regions where hypothesis does not predict Y=1
        # This is essentially 1 minus the sum of lengths of intervals predicted as Y=1
        total_predicted_as_1 = sum(interval[1] - interval[0] for interval in hypothesis_intervals)
        error += (1 - total_predicted_as_1) * 0.1  # Assume the rest of the space is low probability region

        return error
    def experiment_m_range_erm(self, m_first, m_last, step, k, T):
        """Runs the ERM algorithm.
        Calculates the empirical error and the true error.
        Plots the average empirical and true errors.
        Input: m_first - an integer, the smallest size of the data sample in the range.
               m_last - an integer, the largest size of the data sample in the range.
               step - an integer, the difference between the size of m in each loop.
               k - an integer, the maximum number of intervals.
               T - an integer, the number of times the experiment is performed.

        Returns: np.ndarray of shape (n_steps,2).
            A two dimensional array that contains the average empirical error
            and the average true error for each m in the range accordingly.
        """
        ms = range(m_first, m_last + 1, step)
        avg_empirical_errors = []
        avg_true_errors = []

        for m in ms:
            empirical_errors = []
            true_errors = []

            for _ in range(T):
                # Sample data
                samples = self.sample_from_D(m)
                xs, ys = samples[:, 0], samples[:, 1]

                # Find best intervals
                best_intervals, best_error = intervals.find_best_interval(xs, ys, k)

                # Calculate empirical error
                empirical_error = best_error / m
                empirical_errors.append(empirical_error)

                # Calculate true error
                true_error = self.calculate_true_error(best_intervals)
                true_errors.append(true_error)

            # Calculate average errors
            avg_empirical_errors.append(np.mean(empirical_errors))
            avg_true_errors.append(np.mean(true_errors))

        # Plotting the results
        plt.figure(figsize=(10, 5))
        plt.plot(ms, avg_empirical_errors, label='Average Empirical Error')
        plt.plot(ms, avg_true_errors, label='Average True Error')
        plt.xlabel('Sample Size (m)')
        plt.ylabel('Error')
        plt.title('Empirical vs. True Error as a Function of Sample Size')
        plt.legend()
        plt.show()


    def experiment_k_range_erm(self, m, k_first, k_last, step):
        """Finds the best hypothesis for k= 1,2,...,10.
        Plots the empirical and true errors as a function of k.
        Input: m - an integer, the size of the data sample.
               k_first - an integer, the maximum number of intervals in the first experiment.
               m_last - an integer, the maximum number of intervals in the last experiment.
               step - an integer, the difference between the size of k in each experiment.

        Returns: The best k value (an integer) according to the ERM algorithm.
        """
        k_values = range(k_first, k_last + 1, step)
        empirical_errors = []
        true_errors = []

        for k in k_values:
            # Sample data
            samples = self.sample_from_D(m)
            xs, ys = samples[:, 0], samples[:, 1]

            # Find best intervals using ERM algorithm
            best_intervals, empirical_error = intervals.find_best_interval(xs, ys, k)
            empirical_errors.append(empirical_error / m)

            # Estimate true error
            true_error = self.calculate_true_error(best_intervals)
            true_errors.append(true_error)
        print(true_errors)
        # Plot empirical and true errors as a function of k
        plt.figure(figsize=(10, 5))
        plt.plot(k_values, empirical_errors, label='Empirical Error')
        plt.plot(k_values, true_errors, label='True Error')
        plt.xlabel('Number of Intervals (k)')
        plt.ylabel('Error')
        plt.title('Empirical and True Errors as a Function of k')
        plt.legend()
        plt.show()


    def experiment_k_range_srm(self, m, k_first, k_last, step):
        """Run the experiment in (c).
        Plots additionally the penalty for the best ERM hypothesis.
        and the sum of penalty and empirical error.
        Input: m - an integer, the size of the data sample.
               k_first - an integer, the maximum number of intervals in the first experiment.
               m_last - an integer, the maximum number of intervals in the last experiment.
               step - an integer, the difference between the size of k in each experiment.

        Returns: The best k value (an integer) according to the SRM algorithm.
        """
        calculate_penalty = lambda k, n, delta=0.1: np.sqrt((2 * k + np.log(2 / delta)) / n)

        k_values = range(k_first, k_last + 1, step)
        empirical_errors = []
        true_errors = []
        penalties = []
        sums_of_penalty_and_error = []

        for k in k_values:
            # Sample data
            samples = self.sample_from_D(m)
            xs, ys = samples[:, 0], samples[:, 1]

            # Find best intervals using ERM algorithm
            best_intervals, empirical_error = intervals.find_best_interval(xs, ys, k)
            empirical_errors.append(empirical_error / m)

            # Estimate true error
            true_error = self.calculate_true_error(best_intervals)
            true_errors.append(true_error)

            # Calculate penalty
            penalty = calculate_penalty(k, m)
            penalties.append(penalty)

            # Sum of penalty and empirical error
            sum_penalty_error = empirical_error + penalty
            sums_of_penalty_and_error.append(sum_penalty_error)

        plt.figure(figsize=(10, 5))
        plt.plot(k_values, empirical_errors, label='Empirical Error')
        plt.plot(k_values, true_errors, label='True Error')
        plt.plot(k_values, penalties, label='Penalty')
        plt.plot(k_values, sums_of_penalty_and_error, label='Sum of Penalty and Empirical Error')
        plt.xlabel('Number of Intervals (k)')
        plt.ylabel('Error and Penalty')
        plt.title('SRM Analysis as a Function of k')
        plt.legend()
        plt.show()

    def cross_validation(self, m):
        """Finds a k that gives a good test error.
        Input: m - an integer, the size of the data sample.

        Returns: The best k value (an integer) found by the cross validation algorithm.
        """
        # Draw a dataset of n samples
        samples = self.sample_from_D(n)
        # Split into training and validation sets (80% training, 20% validation)
        split_idx = int(m * 0.8)
        training_samples = samples[:split_idx]
        validation_samples = samples[split_idx:]

        training_xs, training_ys = training_samples[:, 0], training_samples[:, 1]
        validation_xs, validation_ys = validation_samples[:, 0], validation_samples[:, 1]

        validation_errors = []
        # Test for k in {1, ..., 10}
        for k in range(1, 11):
            # Train on the training set
            best_intervals, validation_error = intervals.find_best_interval(training_xs, training_ys, k)
            # Evaluate on the validation set
            validation_errors.append(validation_error / m)

        # Select the k with the smallest validation error
        best_k = np.argmin(validation_errors) + 1
        return best_k

    #################################
    # Place for additional methods


    #################################


if __name__ == '__main__':
    ass = Assignment2()
    ass.experiment_m_range_erm(10, 100, 5, 3, 100)
    ass.experiment_k_range_erm(1500, 1, 10, 1)
    ass.experiment_k_range_srm(1500, 1, 10, 1)
    ass.cross_validation(1500)


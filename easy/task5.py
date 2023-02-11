def compare_versions(version_a: str, version_b: str) -> int:
    if version_a == version_b:
        return 0

    version_a_nums = version_a.split('.')
    version_b_nums = version_b.split('.')

    for i in range(min(len(version_a_nums), len(version_b_nums))):
        if version_a_nums[i] > version_b_nums[i]:  # Значит А новее, чем B
            return 1
        elif version_a_nums[i] < version_b_nums[i]:
            return -1

    if len(version_a_nums) > len(version_b_nums):  # Значит version A новее
        return 1
    else:
        return -1

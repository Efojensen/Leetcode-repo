function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    const keyIndices: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === key) {
            keyIndices.push(i);
        }
    }

    const result = new Set<number>();
    for (const j of keyIndices) {
        const start = Math.max(0, j - k);
        const end = Math.min(nums.length - 1, j + k);
        for (let i = start; i <= end; i++) {
            result.add(i);
        }
    }

    return Array.from(result).sort((a, b) => a - b);
}
